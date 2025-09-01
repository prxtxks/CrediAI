import pandas as pd
import numpy as np

def create_features(df):
    """
    Perform feature engineering on the dataset.
    Adds derived features for better model performance.
    """
    # Example: Debt-to-Income Ratio
    if 'debt' in df.columns and 'income' in df.columns:
        df['debt_to_income'] = df['debt'] / df['income']
    
    # Example: Credit Utilization
    if 'credit_used' in df.columns and 'credit_limit' in df.columns:
        df['credit_utilization'] = df['credit_used'] / df['credit_limit']
    
    # Example: Interaction feature
    if 'age' in df.columns and 'income' in df.columns:
        df['income_per_age'] = df['income'] / (df['age'] + 1)  # avoid division by zero
    
    # Fill NaNs with 0
    df = df.fillna(0)
    
    return df