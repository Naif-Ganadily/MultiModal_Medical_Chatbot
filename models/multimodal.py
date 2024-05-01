# Multimodal from huggingface
from transformers import pipeline
from PIL import Image


image_classifier = pipeline(task="image-classification", model="julien-c/hotdog-not-hotdog")
