# RandomForest(200)

## Test Metrics
```json
{
  "roc_auc": 0.9702684199302942,
  "avg_precision": 0.9915584030159322,
  "accuracy": 0.8889489327208863,
  "precision": 0.8798780487804878,
  "recall": 0.9941439889769205,
  "f1": 0.9335274138767589,
  "tn": 404,
  "fp": 394,
  "fn": 17,
  "tp": 2886,
  "train_time": 0.9500038623809814
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
