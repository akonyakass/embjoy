import os
import streamlit as st

st.write("Current Directory:", os.getcwd())
st.write("Files in current directory:", os.listdir("."))
if os.path.exists("images"):
    st.write("Files in 'images' folder:", os.listdir("images"))
else:
    st.write("No 'images' folder found!")
