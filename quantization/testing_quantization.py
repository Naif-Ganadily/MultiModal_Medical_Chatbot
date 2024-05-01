from transformers import AutoModelForCausalLM
import torch

def check_quantization(model):
    for name, module in model.named_modules():
        if isinstance(module, torch.nn.Linear):
            print(f"{name} - {module.weight.dtype}")

model = AutoModelForCausalLM.from_pretrained('ruslanmv/Medical-Llama3-8B')
check_quantization(model)