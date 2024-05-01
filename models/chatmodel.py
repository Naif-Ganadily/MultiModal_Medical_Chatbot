from transformers import pipeline
from dotenv import load_dotenv
import os

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path)
hf_token = os.getenv("HF_TOKEN")

# Ensure the pipeline uses your Hugging Face API token for authorized access
generator = pipeline('text-generation', model='ruslanmv/Medical-Llama3-8B', use_auth_token=hf_token if hf_token else None)

