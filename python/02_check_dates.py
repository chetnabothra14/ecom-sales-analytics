import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
raw_folder = project_root / "data" / "raw"

csv_files = sorted(raw_folder.glob("*.csv"))

for file in csv_files:
    df = pd.read_csv(file)

    df["Created at"] = pd.to_datetime(
        df["Created at"],
        errors="coerce"
    )

    print("=" * 50)
    print(file.name)
    print("Earliest date:", df["Created at"].min())
    print("Latest date:  ", df["Created at"].max())