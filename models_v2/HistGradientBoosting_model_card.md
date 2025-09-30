# HistGradientBoosting

## Test Metrics
```json
{
  "roc_auc": 0.986439358817298,
  "avg_precision": 0.9963139748642957,
  "accuracy": 0.9427181842745204,
  "precision": 0.9574974498469908,
  "recall": 0.9700310024112987,
  "f1": 0.9637234770704997,
  "tn": 673,
  "fp": 125,
  "fn": 87,
  "tp": 2816,
  "train_time": 1.8931660652160645
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
