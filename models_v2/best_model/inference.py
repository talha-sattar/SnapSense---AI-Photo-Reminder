#!/usr/bin/env python3
import sys, os, json, pandas as pd
import joblib
base = os.path.dirname(os.path.abspath(__file__))
info = json.load(open(os.path.join(base, "best_model_info.json")))
schema = info["feature_schema"]
model = joblib.load(os.path.join(base, "CatBoost.joblib"))
if len(sys.argv)!=3:
    print("Usage: python inference.py <input.csv> <output.csv>"); sys.exit(1)
X = pd.read_csv(sys.argv[1])
for col in schema.get('categorical', []):
    if col in X.columns: X[col] = X[col].astype(str)
for col in schema.get('binary', []):
    if col in X.columns: X[col] = X[col].astype(int)
for col in schema.get('numeric', []):
    if col in X.columns: X[col] = X[col].astype(float)
proba = model.predict_proba(X)[:,1]
pred = (proba >= 0.5).astype(int)
pd.DataFrame({"proba":proba,"pred":pred}).to_csv(sys.argv[2], index=False)
print(f"Saved to {sys.argv[2]}")
