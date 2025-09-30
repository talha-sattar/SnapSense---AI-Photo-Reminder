#!/usr/bin/env python3
import sys, pandas as pd
from catboost import CatBoostClassifier, Pool
cb = CatBoostClassifier(); cb.load_model("CatBoost.cbm")
X = pd.read_csv(sys.argv[1])
cat_cols = ['d_o_w', 'day_part', 'location', 'calendar_event', 'contacts_count']
cat_idx = [X.columns.get_loc(c) for c in cat_cols]
pool = Pool(X, cat_features=cat_idx)
proba = cb.predict_proba(pool)[:,1]
pred = (proba >= 0.5).astype(int)
pd.DataFrame({"proba": proba, "pred": pred}).to_csv(sys.argv[2], index=False)
print("Wrote", sys.argv[2])
