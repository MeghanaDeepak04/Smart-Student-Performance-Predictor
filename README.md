#  Smart Student Performance Predictor

A Machine Learning web application that predicts whether a student is likely to **Pass** or **Fail** based on academic and lifestyle factors. The application is built using **Python**, **Scikit-learn**, and **Streamlit**, providing an interactive interface for real-time predictions.


##  Features

- Predicts student academic performance using Machine Learning.
- Performs data preprocessing and feature engineering.
- Trains a Random Forest Classifier for prediction.
- Interactive Streamlit web interface for user input.
- Provides real-time Pass/Fail prediction.
- Displays dataset preview.
- Visualizes student data using charts and graphs.
- Simple, responsive, and user-friendly interface.


## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Streamlit
- Joblib



##  How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/MeghanaDeepak04/Smart-Student-Performance-Predictor.git
```

### 2. Navigate to the Project Folder

```bash
cd Smart-Student-Performance-Predictor
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Train the Machine Learning Model

```bash
python model/train_model.py
```

This command generates:

- `model/student_model.pkl`
- `model/label_encoder.pkl`

### 5. Run the Streamlit Application

```bash
python -m streamlit run app.py
```

### 6. Open in Browser

If the browser does not open automatically, visit:

```text
http://localhost:8501
```


##  Project Structure

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
├── README.md
└── .gitignore
```



## 📊 Output

The application predicts whether a student is likely to:

-  Pass
-  Fail

based on the input values entered by the user.



##  Author

**MeghanaDeepak04**

GitHub: https://github.com/MeghanaDeepak04