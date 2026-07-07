import streamlit as st
import pandas as pd
import joblib
import numpy as np
import matplotlib.pyplot as plt

model = joblib.load("model/student_model.pkl")
label_encoder = joblib.load("model/label_encoder.pkl")
data = pd.read_csv("dataset/student_data.csv")

st.set_page_config(page_title="Student Performance Predictor", page_icon="🎓")

st.title("🎓 Smart Student Performance Predictor")
st.write("This app predicts whether a student will Pass or Fail based on academic and lifestyle factors.")

st.sidebar.header("Enter Student Details")

study_hours = st.sidebar.number_input("Study Hours per Day", 0.0, 12.0, 5.0)
attendance = st.sidebar.number_input("Attendance (%)", 0, 100, 80)
previous_score = st.sidebar.number_input("Previous Score", 0, 100, 70)
sleep_hours = st.sidebar.number_input("Sleep Hours", 0.0, 12.0, 7.0)
assignments_completed = st.sidebar.number_input("Assignments Completed", 0, 10, 8)

if st.sidebar.button("Predict"):
    input_data = np.array([[study_hours, attendance, previous_score, sleep_hours, assignments_completed]])

    prediction = model.predict(input_data)
    result = label_encoder.inverse_transform(prediction)

    if result[0] == "Pass":
        st.success("✅ Prediction: PASS")
    else:
        st.error("❌ Prediction: FAIL")

st.subheader("📊 Dataset Preview")
st.dataframe(data)

st.subheader("📈 Study Hours vs Previous Score")
fig, ax = plt.subplots()
ax.scatter(data["study_hours"], data["previous_score"])
ax.set_xlabel("Study Hours")
ax.set_ylabel("Previous Score")
st.pyplot(fig)

st.subheader("📌 Attendance Distribution")
fig2, ax2 = plt.subplots()
ax2.hist(data["attendance"], bins=5)
ax2.set_xlabel("Attendance (%)")
ax2.set_ylabel("Number of Students")
st.pyplot(fig2)

st.subheader("✅ Project Summary")
st.write("""
This machine learning project predicts student academic performance using factors such as
study hours, attendance, previous score, sleep hours, and assignment completion.
The model is trained using Random Forest Classifier and deployed using Streamlit.
""")