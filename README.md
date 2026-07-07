# Smart Student Performance Predictor

A machine learning web application that predicts whether a student is likely to pass or fail based on academic and lifestyle factors.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib

## Features

- Predicts student performance as Pass or Fail
- Uses study hours, attendance, previous score, sleep hours, and assignments completed
- Performs machine learning prediction using Random Forest Classifier
- Displays dataset preview
- Shows visualizations for study hours, score, and attendance
- Provides an interactive Streamlit dashboard

## Project Structure

```text
Smart-Student-Performance-Predictor/
│
├── dataset/
│   └── student_data.csv
│
├── model/
│   ├── train_model.py
│   ├── student_model.pkl
│   └── label_encoder.pkl
│
├── app.py
├── requirements.txt
└── README.md