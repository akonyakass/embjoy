import os
import streamlit as st
import warnings
import pickle

# Set page configuration for the predictor page
st.set_page_config(page_title="Pregnancy Risk Prediction", layout="wide")
st.title("Pregnancy Risk Prediction")

# Load the trained model from Models/finalized_maternal_model.sav
model_path = os.path.join("Models", "finalized_maternal_model.sav")
try:
    maternal_model = pickle.load(open(model_path, 'rb'))
except Exception as e:
    st.error(f"Error loading prediction model: {e}")

# Predictor introduction
content = (
    "Predicting the risk during pregnancy involves analyzing several parameters, including age, blood sugar levels, "
    "diastolic blood pressure, body temperature, and heart rate. By evaluating these factors using a machine learning model, "
    "we can provide a preliminary risk assessment to guide early interventions and improve maternal outcomes."
)
st.markdown(f"<div style='white-space: pre-wrap;'><b>{content}</b></div></br>", unsafe_allow_html=True)

# Organize user inputs with columns
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

predicted_risk = None

# Buttons for prediction and clear actions
col_button, col_clear = st.columns(2)
with col_button:
    if st.button('Predict Pregnancy Risk'):
        try:
            # Convert inputs to floats
            age = float(age_input)
            diastolicBP = float(diastolicBP_input)
            BS = float(BS_input)
            bodyTemp = float(bodyTemp_input)
            heartRate = float(heartRate_input)
            
            # Make the prediction (model expects a 2D array)
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
        st.experimental_rerun()
