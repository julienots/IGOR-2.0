"""Grille de test : questions jamais vues à l'entraînement + mots-clés attendus.

Usage : python scripts/evaluer.py --model <dossier fusionné>
"""

import argparse
import os
import sys

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "data"))
from igor_dataset import SYSTEM_PROMPT  # noqa: E402

# (question, mots-clés dont au moins la moitié doivent apparaître dans la réponse)
GRILLE = [
    ("Salut, t'es qui toi ?", ["igor", "calisthenics"]),
    ("Quelles étapes pour arriver à la full planche ?", ["tuck", "advanced", "straddle", "full"]),
    ("C'est quoi les étapes du front lever ?", ["tuck", "advanced", "straddle", "full"]),
    ("Combien de tractions il faut pour tenter le muscle-up ?", ["10", "traction"]),
    ("Mon muscle-up bloque quand je dois passer la barre", ["poitrine", "transition", "barre"]),
    ("Le human flag, je commence comment ?", ["vertical", "tuck", "straddle"]),
    ("Je débute, propose-moi un plan d'entraînement", ["traction", "pompe", "dips", "3"]),
    ("Avant le 360 je dois maîtriser quoi ?", ["180", "swing"]),
    ("En planche faut-il les omoplates en protraction ou rétraction ?", ["protraction"]),
    ("Pour le front lever, position des omoplates ?", ["rétraction", "dépression"]),
    ("Comment les juges notent un passage freestyle ?", ["difficulté", "exécution", "fluidité"]),
    ("J'ai mal au coude depuis 2 semaines", ["volume", "médecin", "kiné"]),
    ("Quelle est la capitale de la France ?", ["paris"]),
]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", required=True)
    args = p.parse_args()

    tokenizer = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelForCausalLM.from_pretrained(args.model, dtype=torch.float32)
    reussis = 0
    for q, mots in GRILLE:
        prompt = tokenizer.apply_chat_template(
            [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": q}],
            tokenize=False, add_generation_prompt=True, enable_thinking=False,
        )
        inputs = tokenizer(prompt, return_tensors="pt")
        sortie = model.generate(**inputs, max_new_tokens=250, do_sample=False)
        reponse = tokenizer.decode(sortie[0][inputs["input_ids"].shape[1]:],
                                   skip_special_tokens=True).strip()
        trouves = [m for m in mots if m in reponse.lower()]
        ok = len(trouves) * 2 >= len(mots)
        reussis += ok
        print(f"[{'OK' if ok else 'KO'}] {q}\n    mots trouvés : {trouves} / {mots}\n{reponse}\n")
    print(f"Score : {reussis}/{len(GRILLE)}")


if __name__ == "__main__":
    main()
