import os
import streamlit as st

# Set up the page configuration with an informative title and wide layout
st.set_page_config(page_title="Maternal Mortality: Importance & Impact", layout="wide")
st.title("Maternal Mortality: Importance & Impact")

# --- Section 1: In-depth Introduction & Background ---
st.markdown("""
## Understanding Maternal Mortality

Maternal mortality refers to the death of a woman during pregnancy, childbirth, or within 42 days of delivery due to complications related to these events. It is a critical indicator of the quality of a healthcare system, social equity, and the overall socioeconomic development of a region.

### Why Is This Issue Critical?

- **Human Rights and Equity:**  
  Every maternal death is a tragedy that reflects systemic failures, including inadequate healthcare access, insufficient education, and underlying social inequalities.

- **Economic and Social Impact:**  
  High maternal mortality disrupts families and communities, leading to long-term economic and social challenges. The loss of a mother can have ripple effects on child development and community well-being.

- **Indicator of Healthcare Quality:**  
  Maternal mortality is not just a statistic; it is a measure of how well or how poorly a nation provides care to its most vulnerable population—expectant and new mothers.

Addressing maternal mortality requires targeted, evidence-based interventions and a sustained commitment to improving health infrastructure, policy, and education. The visuals and data presented in this dashboard offer insight into the global trends, regional disparities, and the relationship between human development and maternal health outcomes.
""")

# --- Section 2: Evidence & Detailed Visual Insights ---
st.markdown("## Evidence & Detailed Visual Insights")
st.write("""
The following sections present key visual analyses that underscore the realities of maternal mortality. Each visualization is accompanied by detailed commentary on its findings and implications. These data-driven insights are intended to serve as a call-to-action for policymakers, healthcare providers, and communities.
""")

# Create a function to load an image given its file path in binary mode
def load_image(path):
    with open(path, "rb") as file:
        return file.read()

# Define the desired order as a list of tuples with (filename, detailed description)
ordered_images = [
    (
        "maternal_mortality_ratio_trends.png",
        """
**Mortality Analysis Across Continents Over Years**

This visualization presents an in-depth analysis of maternal mortality ratio trends from 1990 to 2021 across various continents. The chart clearly shows how different regions have fared over the decades, emphasizing both progress made and areas that continue to face significant challenges. It brings attention to the persistent disparities among continents, reflecting differences in healthcare systems, economic development, and governmental policies.
        """
    ),
    (
        "average_maternal_mortality_ratio_continent.png",
        """
**Continental Overview**

This graph summarizes the average maternal mortality ratios for each continent. By providing a continent-level breakdown, the chart makes it easier to compare regions side by side. It highlights which continents have managed to reduce maternal mortality effectively and which remain burdened by higher rates, underlining the critical need for further investment in maternal healthcare in some regions.
        """
    ),
    (
        "average_maternal_mortality_ratio_country.png",
        """
**Country-Level Analysis**

Focusing on individual countries, this detailed chart offers a comparative look at maternal mortality rates on a national scale. The granular analysis sheds light on significant outliers and emphasizes the importance of country-specific strategies. In countries where progress is slow, this visualization serves as a diagnostic tool to identify underlying issues and inform targeted policy interventions.
        """
    ),
    (
        "HDI_Rank_of_Countries_Over_Years.png",
        """
**HDI Rank of Countries Over Years**

This visualization tracks the evolution of Human Development Index (HDI) rankings over the years alongside maternal mortality data. It explores the relationship between human development and maternal health outcomes, demonstrating that improvements in education, income, and life expectancy generally correlate with lower maternal mortality. This graph serves as an important reminder of the broader socioeconomic determinants of health.
        """
    ),
    (
        "Maternal_Mortality_Ratio_VS_Human_Development_Groups.png",
        """
**Maternal Mortality Ratio vs. Human Development Groups**

By contrasting maternal mortality ratios with various human development groups, this graph provides clear evidence of the correlation between a nation’s level of development and its maternal health outcomes. It emphasizes that higher development levels—characterized by better healthcare systems, higher education, and stronger economies—tend to be associated with lower rates of maternal mortality, thus reinforcing the need for integrated development approaches.
        """
    ),
    (
        "Maternal_Mortality_Ratio_across_UNDP_Developing_Regions.png",
        """
**Maternal Mortality Ratio Across UNDP Developing Regions**

This chart examines maternal mortality ratios specifically within regions classified as developing by the United Nations Development Programme (UNDP). It identifies those regions where maternal mortality remains alarmingly high despite global efforts. The visualization is a call-to-action for international collaboration, pinpointing areas where urgent healthcare improvements and investment are necessary to save lives.
        """
    )
]

# Loop through the ordered list and display each image with its detailed description
for filename, description in ordered_images:
    image_path = os.path.join("images", filename)
    try:
        img_data = load_image(image_path)
        st.image(img_data, use_container_width=True)
        st.markdown(description)
        st.write("---")  # Horizontal separator between sections
    except Exception as e:
        st.error(f"Error loading {filename}: {e}")

# --- Section 3: Conclusion and Future Directions ---
st.markdown("## Moving Forward: Strategies for Change")
st.write("""
The comprehensive data and detailed visual evidence presented above shed light on the multifaceted challenges of maternal mortality. They clearly demonstrate that improving maternal health is not solely a medical challenge but also a social, economic, and political imperative.

**Key Strategies for Reducing Maternal Mortality:**

- **Strengthening Healthcare Systems:**  
  Expanding access to quality prenatal, delivery, and postnatal care, particularly in underserved regions.

- **Policy Enhancement:**  
  Implementing robust, evidence-based health policies that focus on maternal well-being and create sustainable healthcare infrastructures.

- **Empowering Communities:**  
  Investing in education and public awareness campaigns, enabling communities to take proactive steps towards improving maternal health.

- **International Collaboration:**  
  Encouraging partnerships among governments, international organizations, and local stakeholders to share resources, expertise, and best practices.

By understanding the trends and insights presented, we can advocate for meaningful, coordinated actions that transform maternal healthcare and save lives around the world.
""")
