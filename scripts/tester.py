"""Pose quelques questions au modèle IGOR fusionné (avant conversion).

Usage : python scripts/tester.py --model <dossier fusionné> ["question" ...]
"""

import argparse
import os
import sys

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "data"))
from igor_dataset import SYSTEM_PROMPT  # noqa: E402

QUESTIONS = [
    "Qui es-tu ?",
    "Comment débloquer mon straddle planche ?",
    "Je fais 6 tractions et 10 dips, fais-moi un programme pour avoir le muscle-up.",
    "C'est quoi la différence entre un 360 et un 540 ?",
    "Donne-moi un combo avec front lever et back lever.",
]


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", required=True)
    p.add_argument("questions", nargs="*")
    args = p.parse_args()

    tokenizer = AutoTokenizer.from_pretrained(args.model)
    model = AutoModelForCausalLM.from_pretrained(args.model, dtype=torch.float32)
    for q in args.questions or QUESTIONS:
        prompt = tokenizer.apply_chat_template(
            [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": q}],
            tokenize=False, add_generation_prompt=True, enable_thinking=False,
        )
        inputs = tokenizer(prompt, return_tensors="pt")
        torch.manual_seed(0)
        sortie = model.generate(**inputs, max_new_tokens=300, do_sample=True,
                                temperature=0.7, top_p=0.9, top_k=40)
        reponse = tokenizer.decode(sortie[0][inputs["input_ids"].shape[1]:],
                                   skip_special_tokens=True)
        print(f"> {q}\n{reponse.strip()}\n")


if __name__ == "__main__":
    main()
