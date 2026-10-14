# IGOR 2.0

IGOR est un coach IA spécialisé en **calisthenics** : statique, force, freestyle, figures,
progressions, transitions, combos, compétitions et programmes d'entraînement.

## Le modèle

- Fichier : [`modele/igor-v2.litertlm`](modele/igor-v2.litertlm) (1,7 Go, stocké avec Git LFS) —
  [téléchargement direct](https://media.githubusercontent.com/media/julienots/IGOR-2.0/ccr-2c045565-tn3tpw/modele/igor-v2.litertlm)
- Ancienne version de test : [`modele/igor-v1.litertlm`](modele/igor-v1.litertlm)
- Base : [Qwen3 1.7B](https://huggingface.co/Qwen/Qwen3-1.7B) (licence Apache 2.0),
  affiné avec LoRA sur les exemples du dossier [`data/`](data/) (156 exemples, 494 avec reformulations)
- Le prompt système d'IGOR est intégré au fichier : il s'applique même si l'appli n'en envoie pas.

IGOR est fiable sur ce qu'il a appris (progressions, programmes, notation en compétition…),
mais peut encore se tromper sur des questions éloignées de ses exemples. Plus il y a
d'exemples dans `data/`, meilleur il est.

Pour l'utiliser sur ton téléphone : télécharge `igor.litertlm` (bouton *Download* sur la page du
fichier), puis importe-le dans ton appli (par exemple Google AI Edge Gallery : bouton **+** →
importer un modèle).

## Améliorer IGOR

Plus il y a d'exemples, meilleur il est. Pour en ajouter, complète les listes de
`data/igor_*.py` (une question et la réponse idéale d'IGOR), puis relance :

```bash
pip install torch transformers peft datasets accelerate litert-torch
python scripts/train.py --base Qwen/Qwen3-1.7B --out igor-merged --epochs 4
python scripts/evaluer.py --model igor-merged
python scripts/export.py --model igor-merged --out export
```

Alternative avec GPU : le notebook [`colab/IGOR_personnalisation.ipynb`](colab/IGOR_personnalisation.ipynb).
