from pathlib import Path
import pandas as pd
import joblib
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.ensemble import IsolationForest

def main():
    root = Path(__file__).resolve().parents[1]
    df = pd.read_csv(root/"data/processed/network_logs_clean.csv")

    X = df[["hour","src_country","bytes_out","request_rate","failed_logins"]]

    pre = ColumnTransformer([
        ("num", Pipeline([("scaler", StandardScaler())]), ["hour","bytes_out","request_rate","failed_logins"]),
        ("cat", OneHotEncoder(handle_unknown="ignore"), ["src_country"]),
    ])

    model = IsolationForest(contamination=0.05, random_state=42)
    pipe = Pipeline([("pre", pre), ("model", model)])

    pipe.fit(X)

    out = root/"outputs"
    out.mkdir(exist_ok=True)
    joblib.dump(pipe, out/"isoforest.joblib")
    print("Saved model to outputs/isoforest.joblib")

if __name__ == "__main__":
    main()
