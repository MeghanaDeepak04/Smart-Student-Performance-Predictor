## How to Run

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

This generates:

- `model/student_model.pkl`
- `model/label_encoder.pkl`

### 5. Run the Streamlit Application

```bash
python -m streamlit run app.py
```

### 6. Open in Browser

If it doesn't open automatically, visit:

```
http://localhost:8501
```