import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Employee Attrition Prediction")
st.write("Predict whether an employee is likely to leave the company.")

# --- Input fields ---
age = st.slider("Age", 18, 60, 30)
daily_rate = st.number_input("Daily Rate (₹)", 100, 1500, 500)
education = st.selectbox("Education Level", ["Below College", "College", "Bachelor", "Master", "Doctor"])
job_role = st.selectbox("Job Role", [
    "Sales Executive",
    "Research Scientist",
    "Laboratory Technician",
    "Manufacturing Director",
    "Healthcare Representative",
    "Manager",
    "Sales Representative",
    "Research Director",
    "Human Resources"
])
marital_status = st.selectbox("Marital Status", ["Single", "Married", "Divorced"])
monthly_income = st.number_input("Monthly Income (₹)", 1000, 100000, 30000)
overtime = st.selectbox("OverTime", ["Yes", "No"])
job_satisfaction = st.selectbox("Job Satisfaction", ["Low", "Medium", "High", "Very High"])
env_satisfaction = st.selectbox("Environment Satisfaction", ["Low", "Medium", "High", "Very High"])
worklife_balance = st.selectbox("Work-Life Balance", ["Bad", "Good", "Better", "Best"])

# --- Convert to numeric using manual mapping ---
education_map = {"Below College": 1, "College": 2, "Bachelor": 3, "Master": 4, "Doctor": 5}
jobrole_map = {
    "Sales Executive": 1, "Research Scientist": 2, "Laboratory Technician": 3,
    "Manufacturing Director": 4, "Healthcare Representative": 5, "Manager": 6,
    "Sales Representative": 7, "Research Director": 8, "Human Resources": 9
}
marital_map = {"Single": 1, "Married": 2, "Divorced": 3}
overtime_map = {"Yes": 1, "No": 0}
satisfaction_map = {"Low": 1, "Medium": 2, "High": 3, "Very High": 4}
worklife_map = {"Bad": 1, "Good": 2, "Better": 3, "Best": 4}

# Map inputs
education_num = education_map[education]
job_role_num = jobrole_map[job_role]
marital_num = marital_map[marital_status]
overtime_num = overtime_map[overtime]
job_satisfaction_num = satisfaction_map[job_satisfaction]
env_satisfaction_num = satisfaction_map[env_satisfaction]
worklife_balance_num = worklife_map[worklife_balance]

# Prepare input array
features = np.array([[age, daily_rate, education_num, job_role_num, marital_num,
                      monthly_income, overtime_num, job_satisfaction_num,
                      env_satisfaction_num, worklife_balance_num]])

# --- Predict ---
if st.button("Predict Attrition"):
    prediction = model.predict(features)[0]
    prediction_proba = model.predict_proba(features)[0][1]  # probability of leaving
    if prediction == 1:
        st.error(f"⚠️ Employee is likely to leave the company. (Chance: {prediction_proba*100:.1f}%)")
    else:
        st.success(f"✅ Employee is likely to stay in the company. (Chance of leaving: {prediction_proba*100:.1f}%)")
