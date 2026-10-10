import pandas as pd
from pathlib import Path

# Project path
project_root = Path(__file__).resolve().parent.parent
cleaned_folder = project_root / "data" / "cleaned"

orders_file = cleaned_folder / "orders.csv"
items_file = cleaned_folder / "order_items.csv"

# Read files
orders = pd.read_csv(orders_file)
items = pd.read_csv(items_file)

print("=" * 60)
print("ORDERS DATASET")
print("=" * 60)

print("Rows:", len(orders))
print("Columns:", len(orders.columns))

print("\nDuplicate Order IDs:")
print(orders["order_id"].duplicated().sum())

print("\nMissing Order IDs:")
print(orders["order_id"].isna().sum())

print("\nMissing values:")
print(orders.isna().sum())

print("\nData types:")
print(orders.dtypes)


print("\n" + "=" * 60)
print("ORDER ITEMS DATASET")
print("=" * 60)

print("Rows:", len(items))
print("Columns:", len(items.columns))

print("\nMissing Order IDs:")
print(items["order_id"].isna().sum())

print("\nMissing Product Names:")
print(items["product_name"].isna().sum())

print("\nMissing Quantity:")
print(items["quantity"].isna().sum())

print("\nMissing Unit Price:")
print(items["unit_price"].isna().sum())

print("\nData types:")
print(items.dtypes)


print("\n" + "=" * 60)
print("ORDER ↔ ITEM CHECK")
print("=" * 60)

order_ids = set(orders["order_id"].dropna())
item_order_ids = set(items["order_id"].dropna())

missing_orders = item_order_ids - order_ids

print("Orders:", len(order_ids))
print("Order IDs appearing in items:", len(item_order_ids))
print("Item Order IDs missing from orders:", len(missing_orders))

if len(missing_orders) == 0:
    print("\n✓ Every order item belongs to an order.")
else:
    print("\n⚠ Some order items have no matching order.")

print("\nQuality check completed.")