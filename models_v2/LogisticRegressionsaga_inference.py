#!/usr/bin/env python3
import sys, pandas as pd
import joblib
pipe = joblib.load("LogisticRegressionsaga.joblib")
X = pd.read_csv(sys.argv[1])
schema = {'target': 'reminder', 'categorical': ['d_o_w', 'day_part', 'location', 'calendar_event', 'contacts_count'], 'binary': ['calendar_active', 'pref_place', 'pref_calendar_event', 'pref_contacts'], 'numeric': ['hour']}
for col in schema.get('categorical', []):
    if col in X.columns: X[col] = X[col].astype(str)
for col in schema.get('binary', []):
    if col in X.columns: X[col] = X[col].astype(int)
for col in schema.get('numeric', []):
    if col in X.columns: X[col] = X[col].astype(float)
proba = pipe.predict_proba(X)[:, 1]
pred = (proba >= 0.5).astype(int)
pd.DataFrame({"proba": proba, "pred": pred}).to_csv(sys.argv[2], index=False)
print(f"Predictions saved to {sys.argv[2]}")
