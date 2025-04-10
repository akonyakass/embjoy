import os
import streamlit as st

# Set the page configuration
st.set_page_config(page_title="Maternal Mortality: Importance & Impact", layout="wide")
st.title("Maternal Mortality: Importance & Impact")

# --- Section 1: Introduction/Bio ---
st.markdown("""
### Why Maternal Mortality Matters

Maternal mortality refers to the death of a woman during pregnancy, childbirth, or within the postpartum period. It is not just a statistic—it represents significant challenges related to healthcare access, social inequality, and gender equity.

Reducing maternal mortality is crucial for the wellbeing of families and communities. It is also a key indicator of the overall quality of healthcare systems and public health policies.  
""")

st.write("""
High maternal mortality rates often highlight systemic issues in healthcare and education. By examining trends and comparing data across regions, we can identify areas for targeted improvement and policy change.
""")

# --- Section 2: Evidence & Visual Insights ---
st.markdown("## Evidence & Visual Insights")
st.write("The following visualizations provide evidence of the current state of maternal mortality. Each image is accompanied by a brief description that explains its significance:")

def load_images_with_filenames(folder_path):
    """
    Load all images in the given folder and return a dictionary mapping
    each filename to its binary data.
    """
    image_dict = {}
    image_filenames = sorted(
        [f for f in os.listdir(folder_path) if f.lower().endswith(('.png', '.jpg', '.jpeg'))]
    )
    for filename in image_filenames:
        full_path = os.path.join(folder_path, filename)
        with open(full_path, "rb") as file:
            image_dict[filename] = file.read()
    return image_dict

# Load images from the "images" folder
images = load_images_with_filenames("images")

# Define descriptions for each image based on filename
descriptions = {
    "maternal_mortality_ratio_trends.png": (
        "This graph shows maternal mortality ratio trends across continents from 1990 to 2021, "
        "highlighting regional differences and key trends over the years."
    ),
    "HDI_Rank_of_Countries_Over_Years.png": (
        "This visualization outlines the evolution of HDI rankings over the years, reflecting shifts in development "
        "and their impact on healthcare systems."
    ),
    "average_maternal_mortality_ratio_continent.png": (
        "This chart presents average maternal mortality ratios by continent, offering a snapshot of global maternal "
        "health disparities."
    ),
    "average_maternal_mortality_ratio_country.png": (
        "A detailed country-level analysis, this graph compares maternal mortality rates across nations to highlight "
        "specific regional challenges."
    ),
    "Maternal_Mortality_Ratio_VS_Human_Development_Groups.png": (
        "This graph contrasts maternal mortality ratios against human development groups, emphasizing the correlation "
        "between economic development and health outcomes."
    ),
    "Maternal_Mortality_Ratio_across_UNDP_Developing_Regions.png": (
        "This image illustrates maternal mortality ratios across different UNDP developing regions, pinpointing areas "
        "that require urgent healthcare intervention."
    )
}

# Display each image along with its description. Only display those images that have a description.
for filename, img_data in images.items():
    # Check if a description is defined for the image file.
    if filename in descriptions:
        st.image(img_data, use_container_width=True)  # Display the image without caption
        st.write(descriptions[filename])              # Display the corresponding description
    else:
        # If a particular file has no defined description, you can simply display the image.
        st.image(img_data, use_container_width=True)

# --- Section 3: Conclusion or Call-to-Action ---
st.markdown("## Moving Forward")
st.write("""
The data and visuals presented highlight the urgent need to address maternal health challenges worldwide. 
Through such insights, policymakers and healthcare providers can work collaboratively to implement more effective strategies 
and drive positive change in maternal healthcare.
""")
