# IGOR 2.0

IGOR est un coach IA spécialisé en **calisthenics** : statique, force, freestyle, figures,
progressions, transitions, combos, compétitions et programmes d'entraînement.

## Le modèle

- Fichier : [`modele/igor.litertlm`](modele/igor.litertlm) (stocké avec Git LFS)
- Base : [Qwen3 0.6B](https://huggingface.co/Qwen/Qwen3-0.6B) (licence Apache 2.0),
  affiné avec LoRA sur les exemples du dossier [`data/`](data/)
- Le prompt système d'IGOR est intégré au fichier : il s'applique même si l'appli n'en envoie pas.

Pour l'utiliser sur ton téléphone : télécharge `igor.litertlm` (bouton *Download* sur la page du
fichier), puis importe-le dans ton appli (par exemple Google AI Edge Gallery : bouton **+** →
importer un modèle).

## Améliorer IGOR

Plus il y a d'exemples, meilleur il est. Pour en ajouter, complète les listes de
`data/igor_*.py` (une question et la réponse idéale d'IGOR), puis relance :

```bash
pip install torch transformers peft datasets accelerate litert-torch
python scripts/train.py --base Qwen/Qwen3-0.6B --out igor-merged
python scripts/export.py --model igor-merged --out export
```

Alternative avec GPU : le notebook [`colab/IGOR_personnalisation.ipynb`](colab/IGOR_personnalisation.ipynb).
