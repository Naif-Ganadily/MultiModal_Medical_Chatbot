from transformers import pipeline
from dotenv import load_dotenv
import os

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '..', '.env')
load_dotenv(dotenv_path)
hf_token = os.getenv("HF_TOKEN")

# Ensure the pipeline uses your Hugging Face API token for authorized access
generator = pipeline('text-generation', model='ruslanmv/Medical-Llama3-8B', use_auth_token=hf_token if hf_token else None)

def askme(question):
    """Generate a response from the model based on the input question."""
    if not isinstance(question, str) or not question.strip():
        raise ValueError("Input must be a non-empty string.")
    
    try:
        # Generate response using the pipeline
        results = generator(question, max_length=100, num_return_sequences=1)
        # Extract the generated text
        response = results[0]['generated_text'] if results else "No response generated."
        return response
    except Exception as e:
        raise Exception(f"An error occurred: {e}")