import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
file = project_root / "data" / "cleaned" / "orders_combined.csv"

df = pd.read_csv(file)

print("Total rows:", len(df))
print("Unique order IDs:", df["Id"].nunique())
print("Rows with an Order ID:", df["Id"].notna().sum())
print("Missing Order IDs:", df["Id"].isna().sum())

print("\nOrders with multiple line items:")
order_counts = df["Id"].value_counts()
print(order_counts[order_counts > 1].head(10))