import pandas as pd
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def remove_customer_id(df):
    """Remove customerID column if it exists"""
    if 'customerID' in df.columns:
        df = df.drop('customerID', axis=1)
        logger.info("Removed customerID column")
    return df

def fix_total_charges(df):
    """Convert TotalCharges to numbers and apply business logic:
    - If tenure == 0, TotalCharges MUST be 0 (even if data says otherwise)
    - Otherwise, fill missing values with median
    """
    df = df.copy()

    # Convert to numeric (bad values become NaN)
    df['TotalCharges'] = pd.to_numeric(df['TotalCharges'], errors='coerce')

    # Count invalid values
    invalid_count = df['TotalCharges'].isna().sum()
    if invalid_count > 0:
        logger.warning(f"Found {invalid_count} invalid TotalCharges values")

    # BUSINESS RULE: tenure == 0 MUST have TotalCharges == 0
    mask_zero_tenure = df['tenure'] == 0
    zero_tenure_with_charges = mask_zero_tenure & (df['TotalCharges'] != 0)
    if zero_tenure_with_charges.any():
        logger.warning(f"Found {zero_tenure_with_charges.sum()} tenure=0 customers with non-zero charges. Correcting to 0.")

    df.loc[mask_zero_tenure, 'TotalCharges'] = 0

    # Fill remaining NaN values (tenure > 0) with median
    remaining_nulls = df['TotalCharges'].isna().sum()
    if remaining_nulls > 0:
        median_val = df['TotalCharges'].median()
        logger.info(f"Filling {remaining_nulls} missing values with median: {median_val}")
        df['TotalCharges'] = df['TotalCharges'].fillna(median_val)

    logger.info(f"TotalCharges fix complete. Data type: {df['TotalCharges'].dtype}")
    return df
