import os
import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Maternal Mortality: Importance & Impact", layout="wide")
st.title("Maternal Mortality: Importance & Impact")

# --- Section 1: Introduction/Bio ---
st.markdown("""
### Why Maternal Mortality Matters

Maternal mortality refers to the death of a woman during pregnancy, childbirth, or within the postpartum period. It is not just a statistic—it represents the significant challenges many countries face regarding access to quality healthcare, social inequality, and gender equity.

Reducing maternal mortality is a crucial goal for ensuring the wellbeing of families and communities. It is a key indicator of the overall quality of healthcare systems, public health policies, and societal development.  
""")

st.write("""
Globally, high maternal mortality rates indicate systemic issues in healthcare access, funding, and education. Analyzing the trends across continents, countries, and socio-economic groups helps in identifying target areas for intervention, driving policy changes, and improving outcomes for mothers and their families.
""")

# --- Section 2: Analysis Evidence with Images ---
st.markdown("## Evidence & Visual Insights")
st.write("Below are a few key visualizations that illustrate trends and patterns in maternal mortality. These images serve as evidence to support our analysis and highlight areas requiring urgent attention:")

# Function to load images from the 'images' folder without using file names for captions
def load_images_from_folder(folder_path):
    # Retrieve files with common image extensions
    image_filenames = sorted(
        [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    )
    images = []
    for filename in image_filenames:
        full_path = os.path.join(folder_path, filename)
        with open(full_path, "rb") as file:
            images.append(file.read())
    return images

# Load images from the 'images' folder
images = load_images_from_folder("images")

# Display the images without captions (you can adjust size using the 'width' parameter)
for img in images:
    st.image(img, use_column_width=True)  # displays each image scaled to the column width

# --- Section 3: Conclusion or Call-to-Action ---
st.markdown("## Moving Forward")
st.write("""
The data and visuals presented herein underscore the pressing need to address maternal health challenges worldwide. By understanding where and why these trends occur, stakeholders can work together to implement effective solutions and bring about positive change in maternal healthcare.
""")
