# multimodal.py
import os
from dotenv import load_dotenv
import requests  # Assuming requests to handle API calls if it's a REST API

# Load environment variables
dotenv_path = os.path.join(os.path.dirname(__file__), '..', '.env')
load_dotenv(dotenv_path)

api_key = os.getenv("GEMINI_API_KEY")

def get_gemini_response(input_prompt, image):
    # Assume Gemini API expects JSON data with image in base64 and text
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "prompt": input_prompt,
        "image": image  # image expected to be in base64
    }
    response = requests.post('https://api.gemini.com/generate', headers=headers, json=data)
    return response.json().get('text', '')  # Ensure to parse response correctly
