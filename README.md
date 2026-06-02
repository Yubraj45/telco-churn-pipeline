# 🏢 Telco Customer Churn Prediction Pipeline

> **Production-grade ML pipeline that predicts customer churn with 79%+ accuracy**


[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.3-orange.svg)](https://scikit-learn.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Code style](https://img.shields.io/badge/code%20style-pep8-blue)](https://www.python.org/dev/peps/pep-0008/)

## 🎯 Business Problem

Customer churn costs telecom companies **billions annually**. This project builds an **end-to-end machine learning pipeline** that:
- Identifies **high-risk customers before they leave** (79%+ accuracy)
- Enables **proactive retention campaigns** (reducing acquisition costs)
- Provides **interpretable predictions** for business teams

**The Impact:** A 5% reduction in churn can increase profits by 25-85% (Bain & Company).

## 🏗️ Architecture
telco_churn_pipeline/
│
├── data/ # Data management
│ ├── raw/ # Original dataset (not in repo)
│ └── processed/ # Cleaned, ready-to-use data
│
├── src/ # Production code
│ ├── clean_data.py # Cleaning with business logic
│ ├── feature_engineering.py # Feature encoding
│ └── prediction_pipeline.py # Production API
│
├── tests/ # Unit tests
│ └── test_clean_data.py # 4+ tests for reliability
│
├── models/ # Trained models (gitignored)
├── configs/ # Configuration files
├── requirements.txt # Dependencies
├── setup.py # Installable package
└── README.md # You're here!



## 🚀 Features

### 1. Smart Data Processing
# Business rule: New customers (tenure=0) must have TotalCharges=0
```
if tenure == 0:
    TotalCharges = 0  # Prevents data contamination
```
    
### 2. Production-Ready Prediction
```from src.prediction_pipeline import ChurnPredictor

predictor = ChurnPredictor()
result = predictor.predict(customer_data)
```
# Output: {'churn_probability': 79.0, 'risk_level': 'HIGH'}


### 3. Robust Error Handling**
* Gracefully handles unknown categories in production
* Logs warnings for data quality issues
* Never crashes - always returns a prediction




**Clone and Install**
```
git clone https://github.com/Yubraj45/telco-churn-pipeline.git
cd telco-churn-pipeline
pip install -r requirements.txt
```


**Make a Prediction**
```
from src.prediction_pipeline import ChurnPredictor

# Load model
predictor = ChurnPredictor()

# Single customer
customer = {
    'gender': 'Female',
    'tenure': 2,
    'Contract': 'Month-to-month',  # High risk!
    'MonthlyCharges': 85.5,
    'TotalCharges': 171.0
}

result = predictor.predict(customer)
print(f"Churn Probability: {result['churn_probability']}%")  # 79.0%
print(f"Risk Level: {result['risk_level']}")  # HIGH
```



**Run Tests**
```
pytest tests/ -v
```



**🧪 Sample Prediction**
==================================================
🔮 CHURN PREDICTION RESULT
==================================================
📊 Churn Probability: 79.0%
⚠️ Will Churn: True
🎯 Risk Level: HIGH
==================================================
💡 RECOMMENDATION: Offer discount or upgrade to long-term contract






**🛠️ Tech Stack**
Category	->  Technologies
Language	->  Python 3.12
Data Processing	-> Pandas, NumPy
Machine Learning	->  Scikit-learn (Random Forest)
Model Persistence	->  Joblib
Testing	->  Pytest
Logging	->  Built-in logging module




**🔄 CI/CD Pipeline (Coming Soon)**
GitHub Actions for automated testing
Model versioning with DVC
Docker containerization
FastAPI REST endpoint
MLflow for experiment tracking



**📈 Key Learnings**
Data Quality > Model Complexity - Simple business rules (tenure=0 → TotalCharges=0) caught bugs that models couldn't learn.
Test Early, Test Often - Unit tests caught the tenure=0 bug before it reached production.
Logging is Non-Negotiable - Without logs, you're blind to data quality issues in production.
Encoder Management - Saved encoders BEFORE transformation (not after) - a classic production pitfall.




**🎓 Future Improvements**
XGBoost/LightGBM for better performance
SHAP values for model interpretability
FastAPI for real-time predictions
Docker for reproducible deployments
Monitoring dashboard (Streamlit/Gradio)



**🤝 Connect**
YUBRAJ SETI SILAL
Linkedin-> https://www.linkedin.com/in/yubraj-seti-silal-65582b274/
GitHub -> https://github.com/Yubraj45



**🙏 Acknowledgments**
IBM Telco Customer Churn Dataset
Scikit-learn documentation
ML Engineering community
