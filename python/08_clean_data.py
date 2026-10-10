import pandas as pd
from pathlib import Path

# ============================================================
# PATHS
# ============================================================

project_root = Path(__file__).resolve().parent.parent
cleaned_folder = project_root / "data" / "cleaned"

orders_file = cleaned_folder / "orders.csv"
items_file = cleaned_folder / "order_items.csv"

# ============================================================
# READ DATA
# ============================================================

orders = pd.read_csv(orders_file)
items = pd.read_csv(items_file)

print("Data loaded successfully.")


# ============================================================
# CLEAN ORDERS DATA
# ============================================================

# Remove completely empty columns
orders = orders.dropna(axis=1, how="all")

# Convert Order ID from float to integer
orders["order_id"] = orders["order_id"].astype("int64")

# Convert date columns
date_columns = [
    "created_at",
    "paid_at",
    "fulfilled_at",
    "cancelled_at"
]

for column in date_columns:
    if column in orders.columns:
        orders[column] = pd.to_datetime(
            orders[column],
            errors="coerce"
        )

# Missing discount code means no discount code was used
orders["discount_code"] = orders["discount_code"].fillna(
    "No Discount"
)

# Missing shipping method
orders["shipping_method"] = orders["shipping_method"].fillna(
    "Unknown"
)

# Missing payment method
orders["payment_method"] = orders["payment_method"].fillna(
    "Unknown"
)

# Missing email
orders["email"] = orders["email"].fillna(
    "Not Available"
)


# ============================================================
# CLEAN ORDER ITEMS DATA
# ============================================================

# Convert Order ID
items["order_id"] = items["order_id"].astype("int64")

# Missing SKU
items["sku"] = items["sku"].fillna(
    "Not Available"
)

# Missing vendor
items["vendor"] = items["vendor"].fillna(
    "Not Available"
)

# Missing fulfillment status
items["fulfillment_status"] = items[
    "fulfillment_status"
].fillna("Unknown")


# ============================================================
# SAVE CLEANED DATA
# ============================================================

orders_output = cleaned_folder / "orders_cleaned.csv"
items_output = cleaned_folder / "order_items_cleaned.csv"

orders.to_csv(
    orders_output,
    index=False
)

items.to_csv(
    items_output,
    index=False
)


# ============================================================
# SUMMARY
# ============================================================

print("\n" + "=" * 60)
print("CLEANING COMPLETED")
print("=" * 60)

print("\nOrders:")
print("Rows:", len(orders))
print("Columns:", len(orders.columns))

print("\nOrder Items:")
print("Rows:", len(items))
print("Columns:", len(items.columns))

print("\nFiles created:")
print(orders_output)
print(items_output)

print("\nRemaining missing values in Orders:")
print(orders.isna().sum())

print("\nRemaining missing values in Order Items:")
print(items.isna().sum())