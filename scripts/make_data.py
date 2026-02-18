from pathlib import Path
import pandas as pd

def main():
    root = Path(__file__).resolve().parents[1]
    raw = root/"data/raw/network_logs.csv"
    out = root/"data/processed/network_logs_clean.csv"
    out.parent.mkdir(parents=True, exist_ok=True)

    df = pd.read_csv(raw).dropna()
    df.to_csv(out, index=False)
    print(f"Wrote: {out} ({len(df)} rows)")

if __name__ == "__main__":
    main()
