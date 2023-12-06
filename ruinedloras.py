import os
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration
from tqdm import tqdm

print("Loading BLIP Captioner...")
model_id = "Salesforce/blip-image-captioning-base"
model = BlipForConditionalGeneration.from_pretrained(model_id)
processor = BlipProcessor.from_pretrained(model_id)

counter = 1

image_directory = "D:\\Portals\\Downloads\\data"
tag_prefix = "<yourtaghere>"


def generate_caption(image):
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs, max_length=20)
    return tag_prefix + ", " + processor.decode(out[0], skip_special_tokens=True)


print("Flipping Images...")
for filename in tqdm(os.listdir(image_directory)):
    if os.path.isfile(os.path.join(image_directory, filename)):
        img = Image.open(os.path.join(image_directory, filename))
        flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        flipped_img.save(os.path.join(image_directory, f"flipped_{filename}"))

print("Renaming and generating captions...")
for filename in tqdm(os.listdir(image_directory)):
    if os.path.isfile(os.path.join(image_directory, filename)):
        new_name = f"{counter}{os.path.splitext(filename)[1]}"
        os.replace(
            os.path.join(image_directory, filename),
            os.path.join(image_directory, new_name),
        )
        img = Image.open(os.path.join(image_directory, new_name))
        caption = generate_caption(img)
        with open(os.path.join(image_directory, f"{counter}.txt"), "w") as f:
            f.write(caption)
        counter += 1
