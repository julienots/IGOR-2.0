"""Convertit le modèle IGOR fusionné en fichier .litertlm.

Le modèle de chat embarqué ajoute automatiquement le prompt système d'IGOR quand l'appli
n'en fournit pas, et désactive le mode « réflexion » de Qwen3 (réponses directes).

Usage : python scripts/export.py --model <dossier fusionné> --out <dossier de sortie>
"""

import argparse
import json
import os
import sys

from litert_torch.generative.export_hf import export as hf_export

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "data"))
from igor_dataset import SYSTEM_PROMPT  # noqa: E402

TEMPLATE = """\
{%- macro texte(c) -%}
{%- if c is string -%}{{ c }}{%- else -%}{%- for p in c -%}{%- if p.type == 'text' -%}{{ p.text }}{%- endif -%}{%- endfor -%}{%- endif -%}
{%- endmacro -%}
{%- if messages[0].role == 'system' -%}
{{- '<|im_start|>system\\n' + texte(messages[0].content) + '<|im_end|>\\n' -}}
{%- else -%}
{{- '<|im_start|>system\\n' + SYSTEME + '<|im_end|>\\n' -}}
{%- endif -%}
{%- for m in messages -%}
{%- if m.role != 'system' -%}
{{- '<|im_start|>' + m.role + '\\n' + texte(m.content) + '<|im_end|>\\n' -}}
{%- endif -%}
{%- endfor -%}
{%- if add_generation_prompt -%}
{{- '<|im_start|>assistant\\n<think>\\n\\n</think>\\n\\n' -}}
{%- endif -%}
""".replace("SYSTEME", json.dumps(SYSTEM_PROMPT, ensure_ascii=False))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", required=True)
    p.add_argument("--out", required=True)
    p.add_argument("--quantization", default="dynamic_wi8_afp32",
                   help="dynamic_wi4_afp32 pour une version légère (téléphones avec peu de RAM)")
    p.add_argument("--cache-length", type=int, default=4096,
                   help="longueur maximale de la conversation, en tokens")
    args = p.parse_args()

    os.makedirs(args.out, exist_ok=True)
    template_path = os.path.join(args.out, "igor_chat_template.jinja")
    with open(template_path, "w") as f:
        f.write(TEMPLATE)

    hf_export.export(
        model=args.model,
        output_dir=args.out,
        jinja_chat_template_override=template_path,
        quantization_recipe=args.quantization,
        cache_length=args.cache_length,
        sampler_temperature=0.7,
        sampler_top_p=0.9,
        sampler_top_k=40,
        # Conversion plus économe en mémoire (nécessaire pour le 1.7B sur 16 Go de RAM).
        experimental_lightweight_conversion=True,
    )


if __name__ == "__main__":
    main()
