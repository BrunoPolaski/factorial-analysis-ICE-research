# pip install factor-analyzer scikit-learn pandas matplotlib
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from factor_analyzer import FactorAnalyzer, calculate_kmo, calculate_bartlett_sphericity
import matplotlib.pyplot as plt

df = pd.read_csv("final.csv")

if 'Cidade' in df.columns:
    df = df.set_index('Cidade')

X_df = df.select_dtypes(include='number').copy()

X_df = X_df.dropna(axis=1, how='all')
X_df = X_df.loc[:, X_df.std(numeric_only=True) > 0]

X_df = X_df.fillna(X_df.median(numeric_only=True))

kmo_vars, kmo_overall = calculate_kmo(X_df)
chi2, p_value = calculate_bartlett_sphericity(X_df)

print(f"KMO overall: {kmo_overall:.3f}")
print(f"Bartlett’s test: chi2 = {chi2:.2f}, p = {p_value:.3e}")

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_df)

fa0 = FactorAnalyzer(rotation=None, method='principal')
fa0.fit(X_scaled)
eigenvalues, _ = fa0.get_eigenvalues()

plt.figure(figsize=(7,5))
plt.scatter(range(1, len(eigenvalues)+1), eigenvalues)
plt.plot(range(1, len(eigenvalues)+1), eigenvalues)
plt.axhline(1, linestyle='--')  # Kaiser threshold
plt.title("Scree Plot (Eigenvalues of Correlation Matrix)")
plt.xlabel("Factor")
plt.ylabel("Eigenvalue")
plt.grid(True)
plt.show()

n_factors = int(np.sum(eigenvalues > 1))
n_factors = max(1, n_factors)
print(f"Chosen number of factors by Kaiser (>1): {n_factors}")

fa = FactorAnalyzer(n_factors=n_factors, rotation='varimax', method='principal')
fa.fit(X_scaled)

loadings = pd.DataFrame(
    fa.loadings_,
    index=X_df.columns,
    columns=[f"Factor{i+1}" for i in range(n_factors)]
).sort_index()

communalities = pd.Series(fa.get_communalities(), index=X_df.columns, name="Communality")
uniqueness = pd.Series(fa.get_uniquenesses(), index=X_df.columns, name="Uniqueness")

var, var_prop, var_cum = fa.get_factor_variance()
variance_df = pd.DataFrame({
    "SS Loadings": var,
    "Proportion Var": var_prop,
    "Cumulative Var": var_cum
}, index=[f"Factor{i+1}" for i in range(n_factors)])

scores = pd.DataFrame(
    fa.transform(X_scaled),
    index=X_df.index,
    columns=[f"Factor{i+1}" for i in range(n_factors)]
)

print("\n=== KMO per variable (first 10) ===")
print(pd.Series(kmo_vars, index=X_df.columns).round(3).head(10))

print("\n=== Loadings (rotated) ===")
print(loadings.round(3))

print("\n=== Variance Explained ===")
print(variance_df.round(3))

print("\n=== First rows of Factor Scores (cities) ===")
print(scores.head().round(3))

loadings.to_csv("fa_loadings.csv")
communalities.to_csv("fa_communalities.csv")
variance_df.to_csv("fa_variance_explained.csv")
scores.to_csv("fa_scores_by_city.csv")