import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import FactorAnalysis

df = pd.read_csv("indicadores.csv")

numeric_values = df.columns[9:-2].values
print("Original data:")
print(df.head())

scaler = StandardScaler()
scaled_values = scaler.fit_transform(df[numeric_values])

df_scaled = pd.DataFrame(scaled_values, index=df.index, columns=df.columns)

print("Data after scaling:")
print(df_scaled.head())