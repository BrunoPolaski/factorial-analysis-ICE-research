import pandas as pd
from sklearn.preprocessing import StandardScaler, MinMaxScaler

df = pd.read_csv("indicadores.csv")

numeric_cols = df.columns[6:]

scaler = StandardScaler()
df_scaled = df.copy()
df_scaled[numeric_cols] = scaler.fit_transform(df[numeric_cols])

# shows std scaled cols per index
for col in numeric_cols:
    print(f"Index: {col}, Values: {df_scaled[col].values}")

subdet_indices = {}
for subdet in df["Subdeterminante"].dropna().unique():
    subset = df[df["Subdeterminante"] == subdet]
    subset_scaled = df_scaled.loc[subset.index, numeric_cols]
    
    subdet_index = subset_scaled.sum(axis=0)
    subdet_indices[subdet] = subdet_index

df_subdet = pd.DataFrame(subdet_indices, index=numeric_cols)

det_indices = {}
for det in df["Determinante"].dropna().unique():
    subdets = df[df["Determinante"] == det]["Subdeterminante"].dropna().unique()
    
    det_index = df_subdet[subdets].sum(axis=1)
    det_indices[det] = det_index

df_det = pd.DataFrame(det_indices, index=numeric_cols)

df_final = pd.concat([df_subdet, df_det], axis=1)

df_final.to_csv("calculated_indexes.csv", index_label="Município")

print("Indexes saved successfully")
