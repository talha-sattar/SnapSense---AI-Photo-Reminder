# BEST MODEL: CatBoost

Selected by ROC AUC on the held-out test set.

## Test Metrics
```json
{
  "roc_auc": 0.9874142814839372,
  "avg_precision": 0.9966069802732489,
  "accuracy": 0.9456903539583896,
  "precision": 0.9604635310156783,
  "recall": 0.9707199448846021,
  "f1": 0.965564502312832,
  "tn": 682,
  "fp": 116,
  "fn": 85,
  "tp": 2818,
  "train_time": 30.705455780029297
}
```

## Feature Schema
```json
{
  "target": "reminder",
  "categorical": [
    "d_o_w",
    "day_part",
    "location",
    "calendar_event",
    "contacts_count"
  ],
  "binary": [
    "calendar_active",
    "pref_place",
    "pref_calendar_event",
    "pref_contacts"
  ],
  "numeric": [
    "hour"
  ]
}
```
