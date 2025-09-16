import streamlit as st
import pandas as pd
import numpy as np
import pickle

st.set_page_config(page_title="Concrete Strength Prediction", page_icon="🏗️", layout="centered")
st.title("Concrete Strength Prediction 🏗️")
st.write("This app predicts the compressive strength of concrete based on its components.")
st.write("Please input the values for each component below:")
# Load the model
@st.cache_resource
def load_model():
    with open("model/compress_model.pkl", "rb") as f:
        model = pickle.load(f) 
    return model

model = load_model()

# Input fields for the features
cement = st.number_input("Cement (kg in a m³ mixture)", min_value=0.0, value=200.0)
blast_furnace_slag = st.number_input("Blast Furnace Slag (kg in a m³ mixture)", min_value=0.0, value=100.0)
fly_ash = st.number_input("Fly Ash (kg in a m³ mixture)", min_value=0.0, value=50.0)
water = st.number_input("Water (kg in a m³ mixture)", min_value=0.0, value=150.0)
superplasticizer = st.number_input("Superplasticizer (kg in a m³ mixture)", min_value=0.0, value=5.0)
coarse_aggregate = st.number_input("Coarse Aggregate (kg in a m³ mixture)", min_value=0.0, value=1000.0)
fine_aggregate = st.number_input("Fine Aggregate (kg in a m³ mixture)", min_value=0.0, value=800.0)
age = st.number_input("Age (days)", min_value=1, value=28) 

# Predict button
if st.button("Predict Compressive Strength"):
    input_data = np.array([[cement, blast_furnace_slag, fly_ash, water, superplasticizer, coarse_aggregate, fine_aggregate, age]])
    prediction = model.predict(input_data)
    st.success(f"The predicted compressive strength of the concrete is {prediction[0]:.2f} MPa")
