"""
Simple feature engineering for Telco Churn
"""

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def encoded_categorical(df, columns_to_encode):
    """Convert categorical columns to numbers"""
    df = df.copy()
    encoders = {}

    for col in columns_to_encode:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col].astype(str))
        encoders[col] = le
        print(f"  Encoded {col}: {dict(zip(le.classes_, le.transform(le.classes_)))}")

    return df, encoders

def prepare_features(df, target_column='Churn'):
    """Split features and target"""
    X = df.drop(target_column, axis=1)
    y = df[target_column]

    # Convert target to binary (Yes=1, No=0)
    y = (y == 'Yes').astype(int)

    return X, y

print("Feature engineering module created successfully!")
