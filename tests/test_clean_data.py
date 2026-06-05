"""
Unit tests for clean_data.py
Run with: pytest tests/test_clean_data.py -v
"""

import pytest
import pandas as pd
import sys
import os

# Add parent directory to path
sys.path.append('/content/telco_churn_pipeline')

from src.clean_data import remove_customer_id, fix_total_charges

def test_remove_customer_id():
    """Test that customerID column is removed"""
    df = pd.DataFrame({
        'customerID': ['A123', 'B456'],
        'Churn': ['Yes', 'No']
    })

    result = remove_customer_id(df)

    # Assertions - if these fail, test fails
    assert 'customerID' not in result.columns
    assert result.shape[1] == 1

def test_fix_total_charges_converts_to_numbers():
    """Test that string numbers become float"""
    df = pd.DataFrame({
        'tenure': [1, 2],
        'TotalCharges': ['123.45', '678.90']
    })

    result = fix_total_charges(df)

    assert result['TotalCharges'].dtype == 'float64'
    assert result['TotalCharges'].iloc[0] == 123.45

def test_fix_total_charges_handles_bad_data():
    """Test that invalid values become 0 for tenure=0 customers"""
    df = pd.DataFrame({
        'tenure': [0, 0],
        'TotalCharges': ['bad_data', 'also_invalid']
    })

    result = fix_total_charges(df)

    # tenure=0 customers should get 0
    assert result['TotalCharges'].iloc[0] == 0
    assert result['TotalCharges'].iloc[1] == 0

def test_fix_total_charges_tenure_zero_rule():
    """Test business rule: tenure=0 MUST have TotalCharges=0"""
    df = pd.DataFrame({
        'tenure': [0, 0, 1],
        'TotalCharges': ['999.99', 'invalid', '100.00']
    })

    result = fix_total_charges(df)

    # Both tenure=0 customers should be 0
    assert result['TotalCharges'].iloc[0] == 0
    assert result['TotalCharges'].iloc[1] == 0
    # tenure=1 customer should keep value
    assert result['TotalCharges'].iloc[2] == 100.00

print("Test file created successfully!")
