import os
import streamlit as st
import warnings
import pickle

# ----------------------------
# Load the trained prediction model
# ----------------------------
# Adjust the path below as needed (ensure the model file is in your repository)
model_path = os.path.join("Models", "maternal_model.pkl")
try:
    with open(model_path, "rb") as f:
        maternal_model = pickle.load(f)
except Exception as e:
    st.error(f"Error loading prediction model: {e}")

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(page_title="Maternal Mortality: Analysis & Prediction", layout="wide")

# Sidebar navigation
options = [
    "Maternal Mortality Analysis",
    "Pregnancy Risk Prediction"
]
selected_option = st.sidebar.radio("Select Section", options)

# ----------------------------
# Maternal Mortality Analysis Section
# ----------------------------
if selected_option == "Maternal Mortality Analysis":
    st.title("Maternal Mortality: Importance & Impact")

    # -- Introduction & Background --
    st.markdown("""
    ## Understanding Maternal Mortality

    Maternal mortality refers to the death of a woman during pregnancy, childbirth, or within 42 days of delivery due to complications related to these events. It is a critical indicator of the quality of healthcare systems, social equity, and overall socioeconomic development.

    ### Why Is This Issue Critical?

    - **Human Rights and Equity:**  
      Each maternal death reflects systemic challenges, including inadequate healthcare, insufficient education, and deep-seated social inequities.

    - **Economic and Social Impact:**  
      High maternal mortality not only disrupts families but also places long-term economic and social burdens on communities.

    - **Indicator of Healthcare Quality:**  
      Maternal mortality is a comprehensive measure of a nation’s ability to provide proper prenatal, delivery, and postnatal care to its citizens.
      
    Addressing maternal mortality requires targeted interventions, policy reforms, and a strong commitment to improving healthcare infrastructure.
    """)

    # -- Evidence & Detailed Visual Insights --
    st.markdown("## Evidence & Detailed Visual Insights")
    st.write("""
    The following visualizations provide robust evidence of the current state of maternal mortality, arranged in a logical sequence:
    
    1. **Mortality analysis across continents over years**
    2. **Continental Overview**
    3. **Country-Level Analysis**
    4. **HDI Rank of Countries Over Years**
    5. **Maternal Mortality Ratio vs. Human Development Groups**
    6. **Maternal Mortality Ratio Across UNDP Developing Regions**
    
    Each visualization is accompanied by an in-depth commentary explaining its significance and the insights it offers.
    """)

    # Function to load an image given its file path in binary mode
    def load_image(path):
        with open(path, "rb") as file:
            return file.read()

    # Define the ordered list of images (filename, detailed description)
    ordered_images = [
        (
            "maternal_mortality_ratio_trends.png",
            """
**Mortality Analysis Across Continents Over Years**

This visualization presents an in-depth analysis of maternal mortality ratio trends from 1990 to 2021 across various continents. It clearly shows the progress and challenges over the decades, highlighting regional disparities in healthcare systems and economic development.
            """
        ),
        (
            "average_maternal_mortality_ratio.png",  # For continental overview
            """
**Continental Overview**

This graph summarizes the average maternal mortality ratios for each continent. It enables direct side-by-side comparisons of the regions, indicating which continents have successfully reduced maternal mortality and which remain challenged.
            """
        ),
        (
            "average_maternal_mortality_ratio_country.png",
            """
**Country-Level Analysis**

This detailed chart offers a country-by-country comparison of maternal mortality rates. The granular analysis provides insights into national trends and highlights outliers that may require special attention through targeted policy interventions.
            """
        ),
        (
            "HDI_Rank_of_Countries_Over_Years.png",
            """
**HDI Rank of Countries Over Years**

This visualization tracks the evolution of Human Development Index (HDI) rankings in relation to maternal mortality data. It demonstrates that improvements in education, income, and health correlate with lower maternal deaths, emphasizing the importance of comprehensive development strategies.
            """
        ),
        (
            "Maternal_Mortality_Ratio_VS_Human_Development_Groups.png",
            """
**Maternal Mortality Ratio vs. Human Development Groups**

By comparing maternal mortality ratios with various human development groups, this graph reveals a strong correlation between a nation's developmental status and its maternal health outcomes. It suggests that higher human development is generally associated with lower maternal mortality.
            """
        ),
        (
            "Maternal_Mortality_Ratio_across_UNDP_Developing_Regions.png",
            """
**Maternal Mortality Ratio Across UNDP Developing Regions**

Focusing on regions classified as developing by the UNDP, this chart provides a detailed look at maternal mortality ratios in areas with significant healthcare challenges. It serves as a call to action, emphasizing the need for focused international aid and policy reforms in these regions.
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

    # -- Conclusion / Call-to-Action --
    st.markdown("## Moving Forward: Strategies for Change")
    st.write("""
    The comprehensive data and insights presented above expose the multifaceted challenges of maternal mortality. Improving maternal health is not solely a medical endeavor—it is intrinsically linked to social, economic, and political progress.

    **Key Strategies for Reducing Maternal Mortality:**
    
    - **Strengthening Healthcare Systems:**  
      Enhance access to quality care by expanding facilities and training healthcare professionals, particularly in underserved regions.
    
    - **Policy Enhancement:**  
      Implement evidence-based policies that prioritize maternal well-being and allocate resources efficiently.
    
    - **Community Empowerment:**  
      Invest in education and public awareness to enable communities to actively participate in improving maternal health.
    
    - **International Collaboration:**  
      Foster cooperation between governments, international organizations, and local stakeholders to share best practices and resources.
    
    Through coordinated efforts, we can make significant strides in reducing maternal mortality and ensuring a healthier future for mothers and their families worldwide.
    """)

# ----------------------------
# Pregnancy Risk Prediction Section
# ----------------------------
elif selected_option == "Pregnancy Risk Prediction":
    st.title("Pregnancy Risk Prediction")
    
    # Detailed introduction about the prediction approach
    content = (
        "Predicting the risk during pregnancy involves analyzing several key parameters such as age, diastolic blood pressure, "
        "blood glucose levels, body temperature, and heart rate. Leveraging a trained machine learning model, we can evaluate "
        "these factors to provide a preliminary risk assessment. This predictive approach not only aids in early detection but "
        "also supports proactive healthcare measures to improve outcomes."
    )
    st.markdown(f"<div style='white-space: pre-wrap;'><b>{content}</b></div></br>", unsafe_allow_html=True)
    
    # Layout for user inputs using columns
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age_input = st.text_input('Age of the Person', key="age")
    with col2:
        diastolicBP_input = st.text_input('Diastolic BP (mmHg)', key="diastolicBP")
    with col3:
        BS_input = st.text_input('Blood Glucose (mmol/L)', key="BS")
    
    with col1:
        bodyTemp_input = st.text_input('Body Temperature (Celsius)', key="bodyTemp")
    with col2:
        heartRate_input = st.text_input('Heart Rate (BPM)', key="heartRate")
    
    # Initialize prediction result
    predicted_risk = None
    
    # Create a button for prediction
    with col1:
        if st.button('Predict Pregnancy Risk'):
            try:
                # Convert inputs to numeric values; use float() or int() as appropriate
                age = float(age_input)
                diastolicBP = float(diastolicBP_input)
                BS = float(BS_input)
                bodyTemp = float(bodyTemp_input)
                heartRate = float(heartRate_input)
                
                # Make prediction; the model expects inputs in a 2D array format
                with warnings.catch_warnings():
                    warnings.simplefilter("ignore")
                    predicted_risk = maternal_model.predict([[age, diastolicBP, BS, bodyTemp, heartRate]])
                
                st.subheader("Risk Level:")
                if predicted_risk[0] == 0:
                    st.markdown('<p style="font-weight: bold; font-size: 20px; color: green;">Low Risk</p>', unsafe_allow_html=True)
                elif predicted_risk[0] == 1:
                    st.markdown('<p style="font-weight: bold; font-size: 20px; color: orange;">Medium Risk</p>', unsafe_allow_html=True)
                else:
                    st.markdown('<p style="font-weight: bold; font-size: 20px; color: red;">High Risk</p>', unsafe_allow_html=True)
            except ValueError:
                st.error("Please enter valid numeric values for all parameters.")
            except Exception as e:
                st.error(f"An error occurred during prediction: {e}")
    
    # Create a Clear button to refresh the form
    with col2:
        if st.button("Clear"):
            st.experimental_rerun()
