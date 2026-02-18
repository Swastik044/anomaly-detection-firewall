from pathlib import Path
import pandas as pd

def test_logs():
    root = Path(__file__).resolve().parents[1]
    df = pd.read_csv(root/"data/raw/network_logs.csv")
    assert len(df) > 1000
    assert {"bytes_out","request_rate","failed_logins","is_anomaly"} <= set(df.columns)
