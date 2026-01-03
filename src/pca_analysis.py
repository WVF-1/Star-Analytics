# src/pca_analysis.py

import pandas as pd
from sklearn.decomposition import PCA

def run_pca(X_scaled, n_components=2):
    """
    Perform PCA and return transformed data + model.
    """
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)
    return X_pca, pca

def pca_dataframe(X_pca: list, df: pd.DataFrame) -> pd.DataFrame:
    """
    Combine PCA output with original labels (if any).
    """
    pca_df = pd.DataFrame(
        X_pca,
        columns=["PC1", "PC2"]
    )
    if "Star type" in df.columns:
        pca_df["Star type"] = df["Star type"].values
    return pca_df
