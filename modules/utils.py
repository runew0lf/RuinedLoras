import os
import pathlib
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch

print("Loading BLIP Captioner...")
model_id = "Salesforce/blip-image-captioning-base"
model = BlipForConditionalGeneration.from_pretrained(model_id)
processor = BlipProcessor.from_pretrained(model_id)
device = "cuda" if torch.cuda.is_available() else "cpu"
model.to(device)


def generate_caption(image, tag_prefix):
    inputs = processor(image, return_tensors="pt")
    inputs.to(device)
    out = model.generate(**inputs, max_length=20)
    return tag_prefix + ", " + processor.decode(out[0], skip_special_tokens=True)
