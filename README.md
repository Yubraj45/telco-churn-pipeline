# telco-churn-pipeline
Production-grade ML pipeline for customer churn prediction
# Telco Customer Churn Prediction Pipeline

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
if tenure == 0:
    TotalCharges = 0  # Prevents data contamination

    
### 2. Production-Ready Prediction
from src.prediction_pipeline import ChurnPredictor

predictor = ChurnPredictor()
result = predictor.predict(customer_data)

# Output: {'churn_probability': 79.0, 'risk_level': 'HIGH'}


### 3. Robust Error Handling**
* Gracefully handles unknown categories in production
* Logs warnings for data quality issues
* Never crashes - always returns a prediction





