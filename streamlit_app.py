import os
import streamlit as st

# Set up the page configuration with an informative title and wide layout
st.set_page_config(page_title="Maternal Mortality: Importance & Impact", layout="wide")
st.title("Maternal Mortality: Importance & Impact")

# --- Section 1: Introduction & In-depth Bio ---
st.markdown("""
## Understanding Maternal Mortality

Maternal mortality is a critical indicator that reflects the quality of healthcare, socioeconomic conditions, and public health policies in a region. It represents the death of a woman during pregnancy, childbirth, or within 42 days of delivery, due to complications related to these processes. Every maternal death is not just a loss of an individual; it reverberates through families, communities, and entire healthcare systems.

### Why Is This Issue Vital?

- **Human Rights & Equity:**  
  Access to quality maternal healthcare is a fundamental human right. Disparities in maternal health outcomes often expose underlying inequities in society.
  
- **Economic and Social Impact:**  
  High maternal mortality rates disrupt families, lower community productivity, and create long-lasting emotional and financial burdens.
  
- **Indicator of Healthcare Systems:**  
  Maternal mortality is considered a sensitive indicator of the overall health infrastructure, as it is influenced by factors like access to skilled care, emergency services, and effective health policies.

Reducing maternal mortality involves addressing deep-rooted issues related to poverty, education, and gender inequality. Evidence-based data and insightful analysis are crucial for developing targeted interventions that can ultimately save lives.
""")

st.write("""
In this dashboard, you will find a series of comprehensive visualizations that not only depict trends but also uncover the systemic issues contributing to maternal mortality. The insights presented here are aimed at educating stakeholders, policymakers, and the general public on the importance of improving maternal health standards globally.
""")

# --- Section 2: Evidence & Detailed Visual Insights ---
st.markdown("## Evidence & Detailed Visual Insights")
st.write("""
The following visualizations serve as robust evidence to understand the complexities and trends in maternal mortality. Each image is accompanied by a thorough explanation of its significance, methodology, and findings. These visual insights are instrumental in highlighting disparities, progress, and areas that need immediate attention.
""")

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

# Define long, detailed descriptions for each image based on its filename
descriptions = {
    "maternal_mortality_ratio_trends.png": (
        "### Maternal Mortality Ratio Trends (1990-2021) by Continent\n\n"
        "This detailed line graph illustrates how maternal mortality ratios have evolved across various continents "
        "over the period from 1990 to 2021. The trends highlight both progress and persistent challenges, revealing that "
        "while some regions have made substantial improvements in reducing maternal deaths, others continue to face high risks. "
        "This visualization underscores the disparities in healthcare access, economic development, and public health policies "
        "that are directly related to maternal health outcomes. It serves as a wake-up call for targeted interventions where "
        "improvements are most needed."
    ),
    "HDI_Rank_of_Countries_Over_Years.png": (
        "### Evolution of HDI Rankings in Relation to Maternal Mortality\n\n"
        "This graph tracks the changes in Human Development Index (HDI) rankings over the years for different countries, "
        "providing an indirect measurement of how socioeconomic factors correlate with maternal mortality trends. As HDI improves, "
        "we typically observe enhancements in healthcare services and maternal health outcomes. Conversely, stagnation or decline in "
        "HDI can often be associated with persistently high maternal mortality rates. The visualization acts as a stark reminder "
        "of the link between human development and the capacity of countries to safeguard maternal health."
    ),
    "average_maternal_mortality_ratio_continent.png": (
        "### Average Maternal Mortality Ratios by Continent\n\n"
        "This chart presents the average maternal mortality ratios segregated by continent. It provides a concise summary of the "
        "regional performance in maternal health care. By comparing these averages, the visualization highlights the stark contrasts "
        "between different parts of the world. It emphasizes that regions with lower average ratios have typically invested more in "
        "healthcare infrastructure and preventive measures, whereas high averages indicate areas that face significant challenges "
        "in delivering consistent maternal care."
    ),
    "average_maternal_mortality_ratio_country.png": (
        "### Country-Level Maternal Mortality Analysis\n\n"
        "Focusing on individual countries, this detailed chart compares maternal mortality rates across nations. The granular "
        "analysis reveals not only which countries are performing well but also those that are lagging behind. By providing a "
        "country-level breakdown, it becomes easier to pinpoint where specific healthcare improvements and policy interventions "
        "are required. This detailed view is critical for governments and international organizations aiming to implement targeted "
        "strategies for improving maternal outcomes."
    ),
    "Maternal_Mortality_Ratio_VS_Human_Development_Groups.png": (
        "### Maternal Mortality vs. Human Development Groups\n\n"
        "This comparative graph juxtaposes maternal mortality ratios against various human development groups. The contrasting trends "
        "highlight how development levels influence healthcare outcomes, especially in maternal health. The underlying data suggests "
        "a strong correlation: regions with higher human development tend to exhibit lower maternal mortality rates. This insight "
        "is crucial for advocating improvements in education, economic growth, and healthcare provisions as integrated parts of a "
        "holistic approach to reducing maternal deaths."
    ),
    "Maternal_Mortality_Ratio_across_UNDP_Developing_Regions.png": (
        "### Maternal Mortality Across UNDP Developing Regions\n\n"
        "Focusing on the regions identified by the United Nations Development Programme (UNDP) as developing, this visualization "
        "provides a critical examination of maternal mortality ratios across these areas. The chart reveals the areas with urgent "
        "needs for healthcare investment and policy reforms. It demonstrates how factors such as poverty, limited access to medical services, "
        "and social instability converge to affect maternal health. This clear portrayal invites international collaboration and targeted "
        "assistance to improve maternal outcomes in vulnerable regions."
    )
}

# Display each image along with its detailed description.
for filename, img_data in images.items():
    if filename in descriptions:
        st.image(img_data, use_container_width=True)  # Display the image scaled to the container
        st.markdown(descriptions[filename])
        st.write("---")  # A horizontal separator for clarity between sections
    else:
        st.image(img_data, use_container_width=True)

# --- Section 3: Conclusion and Future Directions ---
st.markdown("## Moving Forward: Strategies for Improvement")
st.write("""
The comprehensive data and detailed visual evidence presented above highlight the multifaceted challenges of maternal mortality. 
They make it clear that addressing maternal health is not simply a medical issue—it is also deeply intertwined with economic, social, 
and political factors. The path to reducing maternal mortality involves:
  
- **Strengthening Healthcare Infrastructure:**  
  Expanding access to quality prenatal, delivery, and postnatal care, especially in low-resource settings.
  
- **Enhancing Policy and Governance:**  
  Implementing evidence-based policies that focus on maternal health as a critical component of public health.
  
- **Empowering Communities:**  
  Investing in education and social services to improve overall human development and community resilience.
  
- **International Collaboration:**  
  Engaging with global partners to share knowledge, resources, and best practices in tackling maternal mortality.

By understanding the trends and underlying causes through rigorous data analysis, stakeholders can work together to create sustainable change. 
The goal is not just to reduce statistics, but to transform lives and ensure that every mother has access to the care she needs.
""")
