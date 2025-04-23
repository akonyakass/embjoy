import os
import streamlit as st
import warnings
import pickle
from joblib import load 

# --- Page Configuration ---
st.set_page_config(page_title="Maternal Mortality: Analysis & Prediction", layout="wide")

# --- Sidebar Navigation ---
sidebar_options = ['Maternal Mortality Analysis', 'Pregnancy Risk Prediction']
selected_option = st.sidebar.radio("Select Section", sidebar_options)

# =============================================
# Maternal Mortality Analysis Section
# =============================================
if selected_option == 'Maternal Mortality Analysis':
    st.title("Maternal Mortality: Importance & Impact")

    # --- Introduction & Background ---
    st.markdown("""
    ## Understanding Maternal Mortality

    Maternal mortality refers to the death of a woman during pregnancy, childbirth, or within 42 days of delivery due to complications.
    It is a critical indicator of the quality of healthcare systems, social equity, and overall socioeconomic development.

    ### Why Is This Issue Critical?

    - **Human Rights and Equity:**  
      Each maternal death exposes systemic issues in accessing quality healthcare and education.
      
    - **Economic and Social Impact:**  
      High maternal mortality rates disrupt families and burden communities with long-term economic and social challenges.
      
    - **Healthcare Quality Indicator:**  
      It reflects a nation's capacity to provide effective prenatal, delivery, and postnatal care.

    Addressing maternal mortality requires targeted interventions, policy reforms, and a strong commitment to enhancing health services.
    """)

    st.markdown("## Evidence & Detailed Visual Insights")
    st.write("""
    The visualizations below provide detailed insights into maternal mortality trends and disparities. They are displayed in the following order:
      
    1. **Mortality Analysis Across Continents Over Years**  
    2. **Continental Overview**  
    3. **Country-Level Analysis**  
    4. **HDI Rank of Countries Over Years**  
    5. **Maternal Mortality Ratio vs. Human Development Groups**  
    6. **Maternal Mortality Ratio Across UNDP Developing Regions**
      
    Each visualization is followed by an explanation of its significance.
    """)

    # --- Helper Function to Load Images ---
    def load_image(path):
        with open(path, "rb") as file:
            return file.read()

    # --- Ordered List of Images with Descriptions ---
    ordered_images = [
        (
            "maternal_mortality_ratio_trends.png",
            """
**Mortality Analysis Across Continents Over Years**

This visualization presents maternal mortality ratio trends from 1990 to 2021 across various continents. It highlights regional disparities by showing where progress has been made and where significant challenges remain.
            """
        ),
        (
            "average_maternal_mortality_ratio.png",
            """
**Continental Overview**

This graph summarizes average maternal mortality ratios for each continent. It allows for a direct comparison to identify regions that have significantly reduced maternal mortality versus those that still face high rates.
            """
        ),
        (
            "average_maternal_mortality_ratio_country.png",
            """
**Country-Level Analysis**

This chart compares maternal mortality rates at the national level, revealing which countries perform well and which require targeted interventions.
            """
        ),
        (
            "HDI_Rank_of_Countries_Over_Years.png",
            """
**HDI Rank of Countries Over Years**

This visualization correlates changes in Human Development Index (HDI) rankings with maternal mortality trends. It illustrates that improvements in education, income, and overall well-being are generally linked to lower maternal mortality.
            """
        ),
        (
            "Maternal_Mortality_Ratio_VS_Human_Development_Groups.png",
            """
**Maternal Mortality Ratio vs. Human Development Groups**

By comparing maternal mortality ratios across different human development groups, this graph shows how increased development levels are associated with improved maternal health outcomes.
            """
        ),
        (
            "Maternal_Mortality_Ratio_across_UNDP_Developing_Regions.png",
            """
**Maternal Mortality Ratio Across UNDP Developing Regions**

This chart focuses on UNDP-classified developing regions, illustrating where maternal mortality remains critically high. It serves as a call-to-action for international support and policy reform in these vulnerable areas.
            """
        )
    ]

    # --- Display Images with Their Explanations ---
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
    The data and insights presented above reveal the multifaceted challenges of maternal mortality.
    Improvement requires a holistic strategy that combines healthcare system strengthening, policy reform, community empowerment, and international collaboration.
    
    **Key Strategies for Change:**
    
    - **Enhancing Healthcare Access:**  
      Expand and improve maternal care services, especially in high-risk regions.
      
    - **Policy Interventions:**  
      Implement evidence-based policies and allocate resources effectively.
      
    - **Community Education:**  
      Improve awareness and empower communities to support maternal health.
      
    - **Global Partnerships:**  
      Foster collaboration among governments, NGOs, and international organizations to share best practices and resources.
    """)

# =============================================
# Pregnancy Risk Prediction Section
elif selected_option == 'Pregnancy Risk Prediction':
    st.title("Pregnancy Risk Prediction")

    st.markdown("""
    Predicting risk based on five parameters:
    age, diastolic blood pressure, blood glucose, body temperature (°F), and heart rate.
    """)

    # --- Load model and scaler ---
    from joblib import load
    import pickle
    import pandas as pd

    model_path  = os.path.join("Models", "finalized_maternal_model.joblib")
    scaler_path = os.path.join("Models", "scaler.sav")
    
    if st.checkbox("⚠️ Debug: test fixed points"):
        test_points = [
            [25, 75, 5.0, 98.6, 70],    # должно быть Low
            [35, 90, 7.0, 99.5, 85],    # должно быть Medium
            [45,110,12.0,100.4,110]     # должно быть High
        ]
        st.write("Preds:", model.predict(test_points))
        try:
            st.write("Probs:", model.predict_proba(test_points).round(2))
        except:
            pass

