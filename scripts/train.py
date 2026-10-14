"""Affine Qwen3 avec LoRA pour créer IGOR, puis fusionne les poids.

Usage : python scripts/train.py --base <modèle HF ou dossier> --out <dossier fusionné>
"""

import argparse
import os
import sys

import torch
from datasets import Dataset
from peft import LoraConfig, get_peft_model
from transformers import (AutoModelForCausalLM, AutoTokenizer, DataCollatorForSeq2Seq, Trainer,
                          TrainingArguments)

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "data"))
from igor_dataset import SYSTEM_PROMPT, toutes_les_paires  # noqa: E402


def construire_dataset(tokenizer, max_length=768):
    """Tokenise les exemples ; la perte ne porte que sur la réponse d'IGOR."""
    lignes = []
    for q, r in toutes_les_paires():
        prompt = tokenizer.apply_chat_template(
            [{"role": "system", "content": SYSTEM_PROMPT}, {"role": "user", "content": q}],
            tokenize=False, add_generation_prompt=True,
        )
        # Réponse directe, sans phase de « réflexion » (comme enable_thinking=False).
        reponse = "<think>\n\n</think>\n\n" + r + "<|im_end|>\n"
        ids_prompt = tokenizer(prompt, add_special_tokens=False)["input_ids"]
        ids_reponse = tokenizer(reponse, add_special_tokens=False)["input_ids"]
        ids = (ids_prompt + ids_reponse)[:max_length]
        labels = ([-100] * len(ids_prompt) + ids_reponse)[:max_length]
        lignes.append({"input_ids": ids, "attention_mask": [1] * len(ids), "labels": labels})
    return Dataset.from_list(lignes).shuffle(seed=0)


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--base", default="Qwen/Qwen3-0.6B")
    p.add_argument("--out", required=True)
    p.add_argument("--epochs", type=float, default=3)
    p.add_argument("--lr", type=float, default=2e-4)
    args = p.parse_args()

    torch.manual_seed(0)
    tokenizer = AutoTokenizer.from_pretrained(args.base)
    model = AutoModelForCausalLM.from_pretrained(args.base, dtype=torch.float32)
    dataset = construire_dataset(tokenizer)
    print(f"{len(dataset)} exemples")

    model.enable_input_require_grads()  # requis pour le gradient checkpointing avec LoRA
    model = get_peft_model(model, LoraConfig(
        r=32, lora_alpha=64, lora_dropout=0.05, task_type="CAUSAL_LM",
        target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
                        "gate_proj", "up_proj", "down_proj"],
    ))
    model.print_trainable_parameters()

    trainer = Trainer(
        model=model,
        train_dataset=dataset,
        data_collator=DataCollatorForSeq2Seq(tokenizer, padding=True),
        args=TrainingArguments(
            output_dir=args.out + "-lora",
            num_train_epochs=args.epochs,
            learning_rate=args.lr,
            lr_scheduler_type="cosine",
            warmup_steps=5,
            per_device_train_batch_size=1,
            gradient_accumulation_steps=8,
            gradient_checkpointing=True,
            logging_steps=5,
            save_strategy="no",
            report_to="none",
            use_cpu=not torch.cuda.is_available(),
        ),
    )
    trainer.train()

    model = trainer.model.merge_and_unload()
    model.save_pretrained(args.out, safe_serialization=True)
    tokenizer.save_pretrained(args.out)
    print("Modèle fusionné enregistré dans", args.out)


if __name__ == "__main__":
    main()
