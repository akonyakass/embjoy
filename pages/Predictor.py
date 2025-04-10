import os
import streamlit as st
import warnings
import pickle

# Set page configuration for the predictor section
st.set_page_config(page_title="Pregnancy Risk Prediction", layout="wide")
st.title("Pregnancy Risk Prediction")

# Load the trained model from Models/finalized_maternal_model.sav
model_path = os.path.join("Models", "finalized_maternal_model.sav")
try:
    maternal_model = pickle.load(open(model_path, 'rb'))
except Exception as e:
    st.error(f"Error loading prediction model: {e}")

st.markdown("""
Predicting the risk during pregnancy involves analyzing key parameters such as age, diastolic blood pressure, blood glucose levels, body temperature, and heart rate. This tool leverages a trained machine learning model to provide a preliminary risk evaluation that supports early interventions and improved maternal outcomes.
""")

# Initialize text inputs with defaults from session_state (or empty if not present)
col1, col2, col3 = st.columns(3)
with col1:
    age_input = st.text_input('Age of the Person', key="age", value=st.session_state.get("age", ""))
with col2:
    diastolicBP_input = st.text_input('Diastolic BP (mmHg)', key="diastolicBP", value=st.session_state.get("diastolicBP", ""))
with col3:
    BS_input = st.text_input('Blood Glucose (mmol/L)', key="BS", value=st.session_state.get("BS", ""))

with col1:
    bodyTemp_input = st.text_input('Body Temperature (Celsius)', key="bodyTemp", value=st.session_state.get("bodyTemp", ""))
with col2:
    heartRate_input = st.text_input('Heart Rate (BPM)', key="heartRate", value=st.session_state.get("heartRate", ""))

predicted_risk = None

# Buttons for prediction and clearing the inputs
col_button, col_clear = st.columns(2)
with col_button:
    if st.button('Predict Pregnancy Risk'):
        try:
            # Convert inputs to numeric values
            age = float(age_input)
            diastolicBP = float(diastolicBP_input)
            BS = float(BS_input)
            bodyTemp = float(bodyTemp_input)
            heartRate = float(heartRate_input)
            
            # Predict risk using the model (ensure it expects a 2D array)
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

with col_clear:
    if st.button("Clear"): 
            st.rerun()
