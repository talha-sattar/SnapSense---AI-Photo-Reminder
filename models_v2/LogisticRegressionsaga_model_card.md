# LogisticRegression(saga)

## Test Metrics
```json
{
  "roc_auc": 0.9788201989645144,
  "avg_precision": 0.99434307720805,
  "accuracy": 0.9240745744393407,
  "precision": 0.9396378269617707,
  "recall": 0.9652084050981743,
  "f1": 0.9522514868309261,
  "tn": 618,
  "fp": 180,
  "fn": 101,
  "tp": 2802,
  "train_time": 0.9269771575927734
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
