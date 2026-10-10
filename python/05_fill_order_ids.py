import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent

input_file = project_root / "data" / "cleaned" / "orders_combined.csv"
output_file = project_root / "data" / "cleaned" / "orders_with_ids.csv"

df = pd.read_csv(input_file)

print("Before filling:")
print("Missing Order IDs:", df["Id"].isna().sum())

# Fill the Order ID downward
df["Id"] = df["Id"].ffill()

print("\nAfter filling:")
print("Missing Order IDs:", df["Id"].isna().sum())
print("Unique Order IDs:", df["Id"].nunique())

# Save the result
df.to_csv(output_file, index=False)

print("\nSaved:")
print(output_file)