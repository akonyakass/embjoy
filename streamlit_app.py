import os
import streamlit as st

def load_images_from_folder(folder_path):
    image_filenames = sorted(
        [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    )
    images = []
    for filename in image_filenames:
        full_path = os.path.join(folder_path, filename)
        with open(full_path, "rb") as file:
            images.append(file.read())
    return images, image_filenames

st.title("Maternal Mortality Analysis Dashboard")

images, image_names = load_images_from_folder("images")

for img_data, file_name in zip(images, image_names):
    # Remove the file extension
    base_name = os.path.splitext(file_name)[0]  # e.g. "HDI_Rank_of_Countries_Over_Years"
    
    # Optional: replace underscores with spaces and capitalize words
  
    
    st.image(img_data, caption=caption_text)
