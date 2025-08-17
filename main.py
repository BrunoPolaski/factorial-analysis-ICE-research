import pandas as pd
from sklearn.preprocessing import StandardScaler

df = pd.read_csv("indicadores.csv")

# numeric columns = cities
city_cols = df.columns[6:]

# scale each indicator row across cities
df_scaled = df.copy()
scaler = StandardScaler()

for i, row in df.iterrows():
    values = row[city_cols].values.reshape(-1, 1)  # cities as column
    scaled_values = scaler.fit_transform(values).flatten()
    df_scaled.loc[i, city_cols] = scaled_values

# ---- SUBDETERMINANTES ----
subdet_indices = {}
for subdet in df["Subdeterminante"].dropna().unique():
    subset = df[df["Subdeterminante"] == subdet]
    subset_scaled = df_scaled.loc[subset.index, city_cols]
    
    # sum across indicators (row-wise std → now cities are comparable)
    subdet_index = subset_scaled.sum(axis=0)
    subdet_indices[subdet] = subdet_index

df_subdet = pd.DataFrame(subdet_indices, index=city_cols)

# ---- DETERMINANTES ----
det_indices = {}
for det in df["Determinante"].dropna().unique():
    subdets = df[df["Determinante"] == det]["Subdeterminante"].dropna().unique()
    det_index = df_subdet[subdets].sum(axis=1)
    det_indices[det] = det_index

df_det = pd.DataFrame(det_indices, index=city_cols)

# ---- FINAL ----
df_final = pd.concat([df_subdet, df_det], axis=1)
df_final.to_csv("calculated_indexes.csv", index_label="Município")

print("✅ Indexes saved successfully (row-wise scaling)")
