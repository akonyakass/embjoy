import os
import streamlit as st

# Page configuration
st.set_page_config(page_title="Maternal Mortality: Analysis & Impact", layout="wide")
st.title("Maternal Mortality: Importance & Impact")

# --- Introduction & Background ---
st.markdown("""
## Understanding Maternal Mortality

Maternal mortality refers to the death of a woman during pregnancy, childbirth, or within 42 days of delivery due to complications. It is a critical indicator of the quality of healthcare systems, social equity, and socioeconomic development.

### Why Is This Issue Critical?

- **Human Rights and Equity:**  
  Each maternal death reveals systemic challenges in healthcare access and education.
  
- **Economic and Social Impact:**  
  High maternal mortality disrupts families and burdens communities with long-term economic and social challenges.
  
- **Indicator of Healthcare Quality:**  
  It measures a nation's ability to provide adequate prenatal, delivery, and postnatal care.
  
Addressing maternal mortality requires targeted interventions, policy reforms, and an unwavering commitment to improving health services.
""")

# --- Evidence & Detailed Visual Insights ---
st.markdown("## Evidence & Detailed Visual Insights")
st.write("""
The visualizations below provide detailed insights into maternal mortality trends and disparities. The order is as follows:
1. **Mortality Analysis Across Continents Over Years**
2. **Continental Overview**
3. **Country-Level Analysis**
4. **HDI Rank of Countries Over Years**
5. **Maternal Mortality Ratio vs. Human Development Groups**
6. **Maternal Mortality Ratio Across UNDP Developing Regions**

Each visualization is followed by a detailed explanation of its significance.
""")

def load_image(path):
    with open(path, "rb") as file:
        return file.read()

# Ordered list of images and descriptions
ordered_images = [
    (
        "maternal_mortality_ratio_trends.png",
        """
**Mortality Analysis Across Continents Over Years**

This chart shows the maternal mortality ratio trends from 1990 to 2021 across different continents. It highlights regional disparities and indicates where improvements have been made as well as where challenges persist.
        """
    ),
    (
        "average_maternal_mortality_ratio.png",
        """
**Continental Overview**

This graph summarizes average maternal mortality ratios by continent, enabling direct comparisons. It indicates which continents have effectively reduced maternal mortality and which continue to experience higher rates.
        """
    ),
    (
        "average_maternal_mortality_ratio_country.png",
        """
**Country-Level Analysis**

This detailed chart compares maternal mortality rates at the country level. It helps to identify outliers and regional variations, offering a basis for targeted policy interventions.
        """
    ),
    (
        "HDI_Rank_of_Countries_Over_Years.png",
        """
**HDI Rank of Countries Over Years**

This visualization links changes in the Human Development Index (HDI) rankings with maternal mortality trends. It demonstrates that improvements in development generally lead to lower maternal mortality rates.
        """
    ),
    (
        "Maternal_Mortality_Ratio_VS_Human_Development_Groups.png",
        """
**Maternal Mortality Ratio vs. Human Development Groups**

By comparing maternal mortality ratios across different human development groups, this graph underscores the correlation between a nation’s level of development and its maternal health outcomes.
        """
    ),
    (
        "Maternal_Mortality_Ratio_across_UNDP_Developing_Regions.png",
        """
**Maternal Mortality Ratio Across UNDP Developing Regions**

This chart examines maternal mortality ratios specifically within UNDP-classified developing regions, highlighting areas where urgent healthcare improvements and policy interventions are needed.
        """
    )
]

for filename, description in ordered_images:
    image_path = os.path.join("images", filename)
    try:
        img_data = load_image(image_path)
        st.image(img_data, use_container_width=True)
        st.markdown(description)
        st.write("---")
    except Exception as e:
        st.error(f"Error loading {filename}: {e}")

# --- Conclusion / Call-to-Action ---
st.markdown("## Moving Forward: Strategies for Change")
st.write("""
The insights above illustrate the complex challenges of maternal mortality, which is influenced by healthcare quality, socioeconomic conditions, and policy measures.

**Key Strategies for Change:**

- **Strengthening Healthcare Systems:**  
  Improve access to comprehensive maternal care across all regions.
  
- **Policy Reforms:**  
  Implement and support evidence-based policies that enhance maternal health services.
  
- **Community Empowerment:**  
  Educate and empower communities to advocate for better healthcare.
  
- **International Collaboration:**  
  Foster global partnerships to share best practices and resources.

Together, these strategies can pave the way for a significant reduction in maternal mortality worldwide.
""")

