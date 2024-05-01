# Multimodal from huggingface
from transformers import AutoModelForImageClassification, AutoFeatureExtractor
import torch

def initialize_image_model(model_name='huggingface/medical-model-name'):
    # Load the model and its feature extractor
    model = AutoModelForImageClassification.from_pretrained(model_name)
    feature_extractor = AutoFeatureExtractor.from_pretrained(model_name)
    return model, feature_extractor

def analyze_image(model, feature_extractor, image):
    # Preprocess the image and make predictions
    inputs = feature_extractor(images=image, return_tensors="pt")
    outputs = model(**inputs)
    predictions = torch.nn.functional.softmax(outputs.logits, dim=-1)
    top_prediction = predictions.argmax(-1)
    return feature_extractor.id2label[top_prediction.item()]