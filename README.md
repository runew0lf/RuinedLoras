# RuinedLoras Image Captioning Tool

This tool creates a training dataset for Learning with Rationales (LoRAs) for [civit.ai](http://civit.ai/). 

## Installation
To install and configure the tool:

1. Create a Python 3 virtual environment

    ```bash
    python3 -m venv .venv
    ```

2. Activate the virtual environment

    ```bash 
    source .venv/bin/activate
    ```

3. Install the required packages

    ```bash
    pip install -r requirements.txt
    ```

## Configuration
Before running the tool, update the following parameters in the Python script:

```python
image_directory = "path/to/image/folder" # Image folder for captioning
tag_prefix = "<your_prefix_here>" # Prefix to add to image captions
```
## Usage
The tool takes images from the configured folder, creates a flipped copy of each for more varied data, renames them to the Civit format, and generates captions.

To run after configuration:

```bash
pip install -r requirements.txt
```
The output captioned images will be saved in the same directory as the original images.

## About
This tool helps create training data for neural networks. The augmented and captioned images can be used to train LoRAs for conditional image generation.