import streamlit as st
import streamlit.components.v1 as components

st.title('EmbJoy ML app')
st.header("Maternal Mortality Analysis")

st.write("Below is the full analysis of maternal mortality as created in our notebook:")

# Try to load and embed the analysis HTML file.
try:
    # If the file is in the same directory, use:
    with open('analysis.html', 'r', encoding='utf-8') as file:
        html_data = file.read()
    # If it's in a folder (e.g., 'html'), update the file path accordingly:
    # with open('html/analysis.html', 'r', encoding='utf-8') as file:
    #     html_data = file.read()

    # Embed the HTML in the Streamlit app.
    # Adjust the 'height' parameter to suit the content length.
    components.html(html_data, height=800, scrolling=True)
except Exception as e:
    st.error("Could not load the analysis HTML file. Please ensure the file is in the correct location.")
