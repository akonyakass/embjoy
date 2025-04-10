import os
import streamlit as st

def load_images_from_folder(folder_path):
    # Get all image filenames with supported extensions
    image_filenames = sorted(
        [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    )
    images = []
    for filename in image_filenames:
        full_path = os.path.join(folder_path, filename)
        with open(full_path, "rb") as file:
            images.append(file.read())
    return images

st.title("Maternal Mortality Analysis Dashboard")

# Load all images from the "images" folder
images = load_images_from_folder("images")

# Display each image without a caption
for img_data in images:
    st.image(img_data)
