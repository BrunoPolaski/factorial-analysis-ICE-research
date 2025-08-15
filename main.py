import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import FactorAnalysis

df = pd.read_csv("indicadores.csv")

numeric_df = df.apply(pd.to_numeric, errors='coerce')

numeric_df = numeric_df.dropna(axis=1, how='all').dropna(axis=0, how='all')

numeric_df = numeric_df.fillna(numeric_df.mean())

scaler = StandardScaler()
scaled_data = scaler.fit_transform(numeric_df)

n_factors = 3
fa = FactorAnalysis(n_components=n_factors, random_state=42)
fa.fit(scaled_data)

loadings_df = pd.DataFrame(
    fa.components_.T,
    index=numeric_df.columns,
    columns=[f"Factor{i+1}" for i in range(n_factors)]
)

communalities = np.sum(loadings_df**2, axis=1)

loadings_df["Communality"] = communalities
loadings_df = loadings_df.sort_values("Communality", ascending=False)
print(loadings_df)

factor_scores = pd.DataFrame(
    fa.transform(scaled_data),
    columns=[f"Factor{i+1}" for i in range(n_factors)]
)
print("\nFactor Scores:")
print(factor_scores.head())
