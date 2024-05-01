from transformers import pipeline
from dotenv import load_dotenv
import os

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)
hf_token = os.getenv("HF_TOKEN")

def initialize_chat_model():
    generator = pipeline('text-generation', model='ruslanmv/Medical-Llama3-8B', use_auth_token=hf_token)
    return generator

def get_model_response(generator, prompt):
    results = generator(prompt, max_length=50)  
    return results[0]['generated_text']