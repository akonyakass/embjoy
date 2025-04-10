import os
import streamlit as st

st.set_page_config(page_title="Maternal Mortality Analysis Dashboard", layout="wide")
st.title("Maternal Mortality Analysis Dashboard")

def load_images_from_folder(folder_path):
    # Find all files with common image extensions
    image_filenames = sorted(
        [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    )
    images = []
    # Read each file in binary mode
    for filename in image_filenames:
        full_path = os.path.join(folder_path, filename)
        with open(full_path, "rb") as file:
            images.append(file.read())
    return images, image_filenames

# Load all images from the "images" folder
images, image_names = load_images_from_folder("images")

# Display all images with their file names as captions (you can customize the caption display if needed)
for img, name in zip(images, image_names):
    st.image(img, caption=name)
