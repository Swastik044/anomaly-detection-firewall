# Anomaly Detection Firewall (Isolation Forest)

Matches your resume bullet: *Python-based firewall with anomaly detection to block unauthorized access attempts*.

## What this project demonstrates
- Synthetic network log dataset with injected anomalies (~5%).
- Unsupervised anomaly detection using IsolationForest.
- Evaluation vs known anomaly labels (precision/recall).
- Can be extended into a real-time streaming rule in production.

## Quickstart
```bash
python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt
```
```bash
python scripts/make_data.py
```
```bash
python scripts/train.py
```
```bash
python scripts/evaluate.py
```

## Repo structure
- `data/raw/network_logs.csv (included)`
- `scripts/train.py (IsolationForest)`
- `outputs/isoforest.joblib`

## Outputs you should expect
- **Primary metric:** Precision/Recall for anomaly flag (vs injected labels)
