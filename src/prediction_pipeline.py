
# production prediction module

import pandas as pd
import sys
import joblib

class ChurnPredictor:
  def __init__(self, model_path='/content/telco_churn_pipeline/models/churn_model.pkl',
                 encoder_path='/content/telco_churn_pipeline/models/encoders.pkl'):
    self.model= joblib.load(model_path)
    self.encoders= joblib.load(encoder_path)
    print("Predictor loaded and ready")

  def predict(self, customer_data):
    #predict Churn for simple customer
    df= pd.DataFrame([customer_data])

    #Encode categorical columns
    for col, encoder in self.encoders.items():
      if col in df.columns:
        df[col] = encoder.transform(df[col].astype(str))

    #make prediction
    proba = self.model.predict_proba(df)[0,1]
    pred= self.model.predict(df)[0]

    return{
        'churn_probability': round(proba * 100, 2),
            'will_churn': bool(pred),
            'risk_level': 'HIGH' if proba > 0.7 else 'MEDIUM' if proba > 0.3 else 'LOW'
    }

print("Prediction module created")
