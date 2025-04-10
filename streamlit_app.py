import os
import streamlit as st

# Page configuration
st.set_page_config(page_title="Maternal Mortality: Analysis & Impact", layout="wide")
st.title("Maternal Mortality: Importance & Impact")

# --- Introduction & Background ---
st.markdown("""
## Understanding Maternal Mortality

Maternal mortality refers to the death of a woman during pregnancy, childbirth, or within 42 days of delivery due to complications related to these events. It is a critical indicator of the quality of healthcare systems, social equity, and the overall socioeconomic development of a region.

### Why Is This Issue Critical?

- **Human Rights and Equity:**  
  Every maternal death reveals underlying issues in access to quality healthcare and education.
  
- **Economic and Social Impact:**  
  High maternal mortality not only disrupts families but also inflicts long-term economic and social challenges on communities.
  
- **Healthcare Quality Indicator:**  
  It provides a comprehensive measure of a nation’s ability to support its maternal health.
  
Addressing maternal mortality requires focused interventions, policy reforms, and continued commitment to improving healthcare services.
""")

# --- Evidence & Detailed Visual Insights ---
st.markdown("## Evidence & Detailed Visual Insights")
st.write("""
The following visualizations, arranged in a logical sequence, provide detailed insight into the trends and disparities associated with maternal mortality:

1. **Mortality Analysis Across Continents Over Years**
2. **Continental Overview**
3. **Country-Level Analysis**
4. **HDI Rank of Countries Over Years**
5. **Maternal Mortality Ratio vs. Human Development Groups**
6. **Maternal Mortality Ratio Across UNDP Developing Regions**

Each visualization is accompanied by a detailed explanation of its significance.
""")

def load_image(path):
    with open(path, "rb") as file:
        return file.read()

# Ordered list of images and their descriptions
ordered_images = [
    (
        "maternal_mortality_ratio_trends.png",
        """
**Mortality Analysis Across Continents Over Years**

This visualization presents trends in maternal mortality ratios from 1990 to 2021 across different continents. It highlights both the progress and the challenges by displaying regional disparities that stem from differences in healthcare systems, economic development, and policy decisions.
        """
    ),
    (
        "average_maternal_mortality_ratio.png",
        """
**Continental Overview**

This graph provides the average maternal mortality ratios for each continent, enabling comparisons between regions. It underscores which continents have effectively reduced maternal mortality and which still lag behind, emphasizing the need for targeted healthcare improvements.
        """
    ),
    (
        "average_maternal_mortality_ratio_country.png",
        """
**Country-Level Analysis**

Offering a detailed breakdown at the country level, this chart compares maternal mortality rates across individual nations. The analysis identifies outliers and pinpoints where intervention is most critical, guiding targeted policy efforts.
        """
    ),
    (
        "HDI_Rank_of_Countries_Over_Years.png",
        """
**HDI Rank of Countries Over Years**

This visualization correlates changes in Human Development Index (HDI) rankings with trends in maternal mortality. It demonstrates that improvements in education, income, and overall well-being are generally associated with reduced maternal mortality, thereby underscoring the importance of holistic development strategies.
        """
    ),
    (
        "Maternal_Mortality_Ratio_VS_Human_Development_Groups.png",
        """
**Maternal Mortality Ratio vs. Human Development Groups**

This graph contrasts maternal mortality ratios against various human development groups. The analysis reveals a clear relationship where higher development levels correspond with lower maternal mortality, thus emphasizing the role of integrated development policies.
        """
    ),
    (
        "Maternal_Mortality_Ratio_across_UNDP_Developing_Regions.png",
        """
**Maternal Mortality Ratio Across UNDP Developing Regions**

Focusing on regions identified by the UNDP as developing, this chart provides a detailed look at maternal mortality in areas with pronounced healthcare challenges. It serves as a call-to-action for enhanced support and policy reforms in regions that need urgent intervention.
        """
    )
]

# Display images and their detailed descriptions in order
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
The visual evidence and detailed insights presented above highlight the multifaceted challenges of maternal mortality. Improving maternal health is not solely a medical issue—it's intertwined with social, economic, and political factors.

**Key Strategies for Change:**

- **Strengthening Healthcare Systems:**  
  Enhance prenatal, delivery, and postnatal care, especially in underserved regions.

- **Policy Reforms:**  
  Implement evidence-based policies to improve maternal healthcare services and ensure resource allocation.

- **Community Empowerment:**  
  Invest in education and awareness initiatives to empower communities to advocate for better healthcare.

- **International Collaboration:**  
  Foster partnerships between governments, NGOs, and international organizations to share best practices and resources.

Through coordinated actions, we can make significant strides in reducing maternal mortality and securing a healthier future for mothers around the world.
""")
