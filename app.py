import streamlit as st
import joblib
import numpy as np


model = joblib.load("heart_model.pkl")

st.title("❤ Heart Disease Prediction")

age = st.number_input("Age", 20, 100, 50)
sex = st.selectbox("Sex", ['Female','Male'])  # 0 = female, 1 = male
if sex == 'Female':
    sex = 0
else :
    sex = 1

cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
chol = st.number_input("Cholesterol", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120", [0, 1])
restecg = st.selectbox("Resting ECG", [0, 1, 2])
thalach = st.number_input("Max Heart Rate", 60, 220, 150)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.number_input("Oldpeak", 0.0, 10.0, 1.0)
slope = st.selectbox("Slope", [0, 1, 2])

if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                            thalach, exang, oldpeak, slope, ]])
    
    prediction = model.predict(input_data)[0]
    
    if prediction == 1:
        st.error("⚠ Heart Disease Detected")
    else:
        st.success("✅ No Heart Disease Detected")
