from PIL import Image
from tqdm import tqdm
from modules.utils import generate_caption
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
        new_file_path = image_directory / new_name
        while new_file_path.exists():
            counter += 1
            new_name = f"{counter}{filename.suffix}"
            new_file_path = image_directory / new_name
        (image_directory / filename.name).rename(new_file_path)
        img = Image.open(new_file_path)
        caption = generate_caption(img, tag_prefix)
        with open(image_directory / f"{counter}.txt", "w") as f:
            f.write(caption)
        counter += 1
