import streamlit as st

# Chest Pain Type
cp_options = {
    "Typical Angina": 0,
    "Atypical Angina": 1,
    "Non-anginal Pain": 2,
    "Asymptomatic": 3
}
cp = st.selectbox("Chest Pain Type", list(cp_options.keys()))
cp_value = cp_options[cp]

# Resting Blood Pressure
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", 80, 200, 120)

# Cholesterol
chol = st.number_input("Serum Cholesterol (mg/dl)", 100, 600, 200)

# Fasting Blood Sugar
fbs_options = {"≤ 120 mg/dl": 0, "> 120 mg/dl": 1}
fbs = st.selectbox("Fasting Blood Sugar", list(fbs_options.keys()))
fbs_value = fbs_options[fbs]

# Resting ECG
restecg_options = {
    "Normal": 0,
    "ST-T Wave Abnormality": 1,
    "Left Ventricular Hypertrophy": 2
}
restecg = st.selectbox("Resting ECG", list(restecg_options.keys()))
restecg_value = restecg_options[restecg]

# Max Heart Rate
thalach = st.number_input("Maximum Heart Rate Achieved", 60, 220, 150)

# Exercise Induced Angina
exang_options = {"No": 0, "Yes": 1}
exang = st.selectbox("Exercise Induced Angina", list(exang_options.keys()))
exang_value = exang_options[exang]

# Oldpeak
oldpeak = st.number_input("ST Depression (Oldpeak)", 0.0, 10.0, 1.0)

# Slope
slope_options = {
    "Upsloping": 0,
    "Flat": 1,
    "Downsloping": 2
}
slope = st.selectbox("Slope of Peak Exercise ST Segment", list(slope_options.keys()))
slope_value = slope_options[slope]
