import os
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

model_id = "Salesforce/blip-image-captioning-base"
model = BlipForConditionalGeneration.from_pretrained(model_id)
processor = BlipProcessor.from_pretrained(model_id)

counter = 1
directory = "D:\\Portals\\Downloads\\data"


def generate_caption(image):
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs, max_length=20)
    return processor.decode(out[0], skip_special_tokens=True)


for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        img = Image.open(os.path.join(directory, filename))
        flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        flipped_img.save(os.path.join(directory, f"flipped_{filename}"))

for filename in os.listdir(directory):
    if os.path.isfile(os.path.join(directory, filename)):
        new_name = f"{counter}{os.path.splitext(filename)[1]}"
        os.rename(os.path.join(directory, filename), os.path.join(directory, new_name))
        img = Image.open(os.path.join(directory, new_name))
        caption = generate_caption(img)
        with open(os.path.join(directory, f"{counter}.txt"), "w") as f:
            f.write(caption)
        counter += 1
