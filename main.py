import os
from PIL import Image

# Input and output folder paths
input_folder = "images"       # Folder containing original images
output_folder = "resized"     # Folder to save resized images
new_size = (800, 800)         # New width, height in pixels

# Create output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Loop through all files in the input folder
for filename in os.listdir(input_folder):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif", ".webp")):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        try:
            # Open image
            img = Image.open(input_path)
            # Resize image
            img_resized = img.resize(new_size, Image.LANCZOS)
            # Save resized image
            img_resized.save(output_path)
            print(f"Resized and saved: {output_path}")
        except Exception as e:
            print(f"Error processing {filename}: {e}")

print("All images processed!")
