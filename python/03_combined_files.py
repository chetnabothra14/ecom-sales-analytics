import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
raw_folder = project_root / "data" / "raw"
cleaned_folder = project_root / "data" / "cleaned"

cleaned_folder.mkdir(parents=True, exist_ok=True)

csv_files = sorted(raw_folder.glob("*.csv"))

dataframes = []

for file in csv_files:
    print(f"Reading: {file.name}")
    df = pd.read_csv(file)
    dataframes.append(df)

# Combine all files
combined_df = pd.concat(dataframes, ignore_index=True)

# Convert Created at to date/time
combined_df["Created at"] = pd.to_datetime(
    combined_df["Created at"],
    errors="coerce"
)

# Sort chronologically
combined_df = combined_df.sort_values(
    by="Created at",
    ascending=True
).reset_index(drop=True)

# Save
output_file = cleaned_folder / "orders_combined.csv"
combined_df.to_csv(output_file, index=False)

print("\nDone!")
print(f"Total rows: {len(combined_df)}")
print(f"Total columns: {len(combined_df.columns)}")
print(f"Earliest date: {combined_df['Created at'].min()}")
print(f"Latest date: {combined_df['Created at'].max()}")
print(f"Saved to: {output_file}")