import torch
from transformers import AutoModelForCausalLM
from torch.quantization import quantize_dynamic

def load_and_quantize_model(model_name, save_directory):
    # Load the model
    model = AutoModelForCausalLM.from_pretrained(model_name)
    
    # Manually specifying layers for quantization
    # Adjust these based on actual model architecture and your inspection results
    layers_to_quantize = [
        'layers.{}.self_attn.q_proj'.format(i) for i in range(32)] + \
        ['layers.{}.self_attn.k_proj'.format(i) for i in range(32)] + \
        ['layers.{}.self_attn.v_proj'.format(i) for i in range(32)] + \
        ['layers.{}.self_attn.o_proj'.format(i) for i in range(32)] + \
        ['layers.{}.mlp.gate_proj'.format(i) for i in range(32)] + \
        ['layers.{}.mlp.up_proj'.format(i) for i in range(32)] + \
        ['layers.{}.mlp.down_proj'.format(i) for i in range(32)]

    # Apply dynamic quantization to specified layers
    for layer_path in layers_to_quantize:
        submodule = dict(model.named_modules())[layer_path]
        quantize_dynamic(submodule, {torch.nn.Linear}, dtype=torch.qint8)

    # Save the quantized model
    model.save_pretrained(save_directory)
    print(f"Quantized model saved at {save_directory}")

if __name__ == "__main__":
    model_name = 'ruslanmv/Medical-Llama3-8B'
    save_directory = './quantized_model'
    load_and_quantize_model(model_name, save_directory)