## Image Resizer Tool
This Python script resizes all images in a given folder using the Pillow (PIL) library and saves them to an output folder.

## Features
Reads all images from an input folder.

Resizes images to a specified size (default: 800×800 pixels).

Saves resized images in a separate output folder.

Supports multiple formats: .png, .jpg, .jpeg, .bmp, .gif, .webp.

## Requirements
Install Pillow:

bash
Copy
Edit
pip install pillow
Usage
Place your images in the images folder (or change the input_folder path in the script).

Set your desired output size in the new_size variable.


Edit
python resize_images.py
Resized images will appear in the resized folder.
