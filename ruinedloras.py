from PIL import Image
from tqdm import tqdm
from modules.utils import get_image_files, generate_caption
from pathlib import Path

counter = 1

tag_prefix = "orangeblack"
image_directory = Path("D:/Portals/Downloads/data/")

print("Flipping Images...")
for filename in tqdm(image_directory.iterdir()):
    if filename.is_file():
        img = Image.open(filename)
        flipped_img = img.transpose(Image.FLIP_LEFT_RIGHT)
        flipped_img.save(image_directory / f"flipped_{filename.name}")

print("Renaming and generating captions...")
for filename in tqdm(image_directory.iterdir()):
    if filename.is_file():
        new_name = f"{counter}{filename.suffix}"
        (image_directory / filename.name).rename(image_directory / new_name)
        img = Image.open(image_directory / new_name)
        caption = generate_caption(img, tag_prefix)
        with open(image_directory / f"{counter}.txt", "w") as f:
            f.write(caption)
        counter += 1
