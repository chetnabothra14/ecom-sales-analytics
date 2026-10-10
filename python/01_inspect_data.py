import pandas as pd
from pathlib import Path

# Project paths
project_root = Path(__file__).resolve().parent.parent
raw_folder = project_root / "data" / "raw"

# Find all CSV files
csv_files = list(raw_folder.glob("*.csv"))

print(f"Found {len(csv_files)} CSV files\n")

for file in csv_files:
    print("=" * 60)
    print(f"FILE: {file.name}")
    print("=" * 60)

    df = pd.read_csv(file)

    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 3 rows:")
    print(df.head(3))

    print("\n")
