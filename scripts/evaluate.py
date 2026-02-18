from pathlib import Path
import pandas as pd
import joblib
from sklearn.metrics import classification_report

def main():
    root = Path(__file__).resolve().parents[1]
    df = pd.read_csv(root/"data/processed/network_logs_clean.csv")
    pipe = joblib.load(root/"outputs/isoforest.joblib")

    X = df[["hour","src_country","bytes_out","request_rate","failed_logins"]]
    # IsolationForest outputs -1 for anomaly, 1 for normal
    pred = pipe.predict(X)
    pred_anom = (pred == -1).astype(int)

    print(classification_report(df["is_anomaly"].astype(int), pred_anom, digits=3))

if __name__ == "__main__":
    main()
