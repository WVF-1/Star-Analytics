# src/clustering.py

import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

def run_kmeans(X, n_clusters=6, random_state=42):
    """
    Fit K-Means clustering.
    """
    model = KMeans(
        n_clusters=n_clusters,
        random_state=random_state,
        n_init=10
    )
    labels = model.fit_predict(X)
    return model, labels

def evaluate_clusters(X, labels):
    """
    Compute silhouette score to assess cluster quality.
    """
    score = silhouette_score(X, labels)
    return score

def attach_clusters(df: pd.DataFrame, labels) -> pd.DataFrame:
    """
    Append cluster labels to dataframe.
    """
    df = df.copy()
    df["Cluster"] = labels
    return df
