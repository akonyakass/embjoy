import os
import streamlit as st

def load_images_from_folder(folder_path):
    # Get a list of image filenames (you can modify the extensions list as needed)
    image_filenames = sorted(
        [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    )
    
    images = []
    for filename in image_filenames:
        full_path = os.path.join(folder_path, filename)
        with open(full_path, "rb") as file:
            images.append(file.read())
    return images, image_filenames

# Example: Load all images in the "images" folder
images, image_names = load_images_from_folder("images")

# Display all images with their file name as caption
for img, name in zip(images, image_names):
    st.image(img, caption=name)
