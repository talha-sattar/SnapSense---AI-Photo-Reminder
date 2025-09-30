# LightGBM

## Test Metrics
```json
{
  "roc_auc": 0.9842048282953335,
  "avg_precision": 0.9957122137969913,
  "accuracy": 0.9421777897865442,
  "precision": 0.9587171613783692,
  "recall": 0.9679641749913882,
  "f1": 0.9633184778882413,
  "tn": 677,
  "fp": 121,
  "fn": 93,
  "tp": 2810,
  "train_time": 1.159177541732788
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
