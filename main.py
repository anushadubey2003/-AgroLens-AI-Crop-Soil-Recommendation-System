import streamlit as st
import pandas as pd
from app.api import recommend_crop, get_fertilizer_suggestion

st.title("AgroLens – Crop & Soil Recommendation System")

st.sidebar.header("Input Parameters")
soil_type = st.sidebar.selectbox("Select Soil Type", ['Loamy', 'Sandy', 'Clay', 'Silty', 'Peaty', 'Chalky'])
ph_level = st.sidebar.slider("Soil pH Level", 3.0, 9.0, 6.5)
rainfall = st.sidebar.slider("Average Monthly Rainfall (mm)", 0, 500, 100)
temperature = st.sidebar.slider("Average Temperature (°C)", -10, 50, 25)

if st.sidebar.button("Get Recommendation"):
    crop = recommend_crop(soil_type, ph_level, rainfall, temperature)
    fertilizer = get_fertilizer_suggestion(soil_type, crop)
    st.success(f"Recommended Crop: {crop}")
    st.info(f"Suggested Fertilizer: {fertilizer}")
