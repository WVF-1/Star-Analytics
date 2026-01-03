# src/data_processing.py

import pandas as pd
from sklearn.preprocessing import StandardScaler

FEATURE_COLS = [
    "Temperature (K)",
    "Luminosity(L/Lo)",
    "Radius(R/Ro)",
    "Absolute magnitude(Mv)"
]

def load_data(path: str) -> pd.DataFrame:
    """Load raw stars dataset."""
    return pd.read_csv(path)

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning:
    - Select numerical astrophysical features
    - Drop missing values
    """
    df = df.copy()
    df = df.dropna(subset=FEATURE_COLS)
    return df

def scale_features(df: pd.DataFrame):
    """
    Standardize numerical features for PCA & K-Means.
    Returns scaled array and fitted scaler.
    """
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df[FEATURE_COLS])
    return X_scaled, scaler
