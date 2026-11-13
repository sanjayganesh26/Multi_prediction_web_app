# Multi Disease Prediction Web Application

A Machine Learning web application built with **Python** and **Streamlit** that provides predictions for three health conditions:

- Diabetes
- Heart disease
- Parkinson's disease

The application presents a separate input form for each condition. Users select a prediction module from the sidebar, enter the required health-related measurements, and submit them to the corresponding pre-trained machine learning model.

> **Disclaimer:** This project is for educational and demonstration purposes only. Its predictions are not a medical diagnosis and must not be used as a substitute for advice from a qualified healthcare professional.

## Features

- Three prediction modules in one Streamlit application.
- Sidebar navigation using `streamlit-option-menu`.
- Separate pre-trained model files for diabetes, heart disease, and Parkinson's disease.
- Input forms arranged into columns for easier data entry.
- Prediction results displayed in the web interface.
- Five-decimal-place input formatting for Parkinson's disease measurements.

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application programming |
| Streamlit | Web application interface |
| Streamlit Option Menu | Sidebar navigation |
| Scikit-learn | Loading and running the trained ML estimators |
| Pickle | Loading serialized model files |

The prediction models are stored as `.sav` files and loaded with Python's `pickle` module.

## Project Structure

The application code expects the model files to be inside a `models` directory:

```text
multi_prediction_web_app/
│
├── multi_prediction.py
├── models/
│   ├── diabetes_model.sav
│   ├── heart_model.sav
│   └── parkinson_model.sav
│
├── requirements.txt
└── README.md
```

## Prediction Inputs

The application currently sends the following input features to each model, in this order:

### 1. Diabetes Prediction

1. Pregnancies
2. Glucose
3. Blood Pressure
4. Skin Thickness
5. Insulin
6. BMI
7. Diabetes Pedigree Function
8. Age

### 2. Heart Disease Prediction

1. Age
2. Sex
3. Chest Pain Type (`cp`)
4. Resting Blood Pressure (`trestbps`)
5. Cholesterol (`chol`)
6. Fasting Blood Sugar (`fbs`)
7. Resting ECG (`restecg`)
8. Maximum Heart Rate (`thalach`)
9. Exercise-Induced Angina (`exang`)
10. Oldpeak
11. Slope
12. Number of Major Vessels (`ca`)
13. Thal

### 3. Parkinson's Disease Prediction

1. MDVP:Fo(Hz)
2. MDVP:Fhi(Hz)
3. MDVP:Flo(Hz)
4. MDVP:Jitter(%)
5. MDVP:Jitter(Abs)
6. MDVP:RAP
7. MDVP:PPQ
8. Jitter:DDP
9. MDVP:Shimmer
10. MDVP:Shimmer(dB)
11. Shimmer:APQ3
12. Shimmer:APQ5
13. MDVP:APQ
14. Shimmer:DDA
15. NHR
16. HNR
17. RPDE
18. DFA
19. spread1
20. spread2
21. D2
22. PPE

**Important:** Keep the feature order consistent with the order used when training each model. Changing the order can produce incorrect predictions or errors.

## Getting Started

### Prerequisites

- Python installed
- `pip` package installer

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

### 2. Move into the project directory

```bash
cd multi_prediction_web_app
```

### 3. Create and activate a virtual environment (recommended)

Windows PowerShell:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

If you have a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install the main packages:

```bash
pip install streamlit streamlit-option-menu scikit-learn
```

### 5. Run the application

```bash
streamlit run multi_prediction.py
```

Streamlit will provide a local URL in the terminal. Open that URL in your browser to use the application.

## Model Files

Place these model files in the `models/` directory:

- `diabetes_model.sav`
- `heart_model.sav`
- `parkinson_model.sav`

The application loads each file with `pickle`. Only load model files from sources you trust: loading a pickle file can execute code.

## Notes for Running on Another Computer

The uploaded application currently uses absolute Windows file paths pointing to one particular computer. Those paths will not work on another machine.

For portability, update the model-loading code to use paths relative to the project directory. For example:

```python
from pathlib import Path
import pickle

MODEL_DIR = Path(__file__).resolve().parent / "models"

diabetes_model = pickle.load(open(MODEL_DIR / "diabetes_model.sav", "rb"))
heart_model = pickle.load(open(MODEL_DIR / "heart_model.sav", "rb"))
parkinson_model = pickle.load(open(MODEL_DIR / "parkinson_model.sav", "rb"))
```

Also ensure the installed Scikit-learn version is compatible with the version used to train and save the models.

## Current Project Scope

This README describes the functionality and input features visible in the supplied application code. The training datasets, model algorithms, training process, evaluation metrics, and model accuracies were not specified in that code, so they are not stated here.

## Author

**Sanjay Ganesh**  
AI & Data Science Student
