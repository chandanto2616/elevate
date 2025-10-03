import os
from PIL import Image

# Input and Output folders
input_folder = "input_images"      # folder where you put images
output_folder = "output_images"    # folder where resized/converted images will be saved

# Create output folder if it doesn’t exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Resize dimensions (width, height)
new_size = (300, 300)

# Output format (choose: "JPEG", "PNG", "WEBP", etc.)
output_format = "JPEG"

# Loop through all files in input_images folder
for file_name in os.listdir(input_folder):
    file_path = os.path.join(input_folder, file_name)

    try:
        # Open the image
        img = Image.open(file_path)

        # Resize the image
        resized_img = img.resize(new_size)

        # Prepare new file name (convert extension)
        base_name, _ = os.path.splitext(file_name)
        new_file_name = f"{base_name}.{output_format.lower()}"
        output_path = os.path.join(output_folder, new_file_name)

        # Save resized + converted image
        resized_img.save(output_path, output_format)
        print(f"✅ Saved: {output_path}")

    except Exception as e:
        print(f"⚠️ Skipped {file_name}: {e}")
