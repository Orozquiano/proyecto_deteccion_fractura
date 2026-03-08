from transformers import AutoImageProcessor, AutoModelForImageClassification
import torch
from app.config import MODEL_NAME, DEVICE

processor = AutoImageProcessor.from_pretrained(MODEL_NAME)
model = AutoModelForImageClassification.from_pretrained(MODEL_NAME)

model.to(DEVICE)
model.eval()