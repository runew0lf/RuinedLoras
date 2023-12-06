# RuinedLoras

This is mainly for creating a training dataset for LoRA's for civit.ai
To get started: `pip install -r requirements.txt`
edit the python script to change the following 2 lines:

`image_directory = "D:\\Portals\\Downloads\\data"` - This is the directory where RuinedLoras will look for the images
and
`tag_prefix = "<yourtaghere>"` - This is your prefix to add at the front of the captioning

What it does: It takes each image, creates a flipped copy (for better training data), renames them all to the civit format and then cpations them
