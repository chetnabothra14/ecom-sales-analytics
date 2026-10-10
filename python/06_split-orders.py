import pandas as pd
from pathlib import Path

# Project folders
project_root = Path(__file__).resolve().parent.parent
input_file = project_root / "data" / "cleaned" / "orders_with_ids.csv"
output_folder = project_root / "data" / "cleaned"

# Read cleaned data
df = pd.read_csv(input_file)

print("Loaded data")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# ============================================================
# 1. CREATE ORDER ITEMS TABLE
# ============================================================

item_columns = [
    "Id",
    "Lineitem name",
    "Lineitem quantity",
    "Lineitem price",
    "Lineitem compare at price",
    "Lineitem sku",
    "Lineitem requires shipping",
    "Lineitem taxable",
    "Lineitem fulfillment status",
    "Lineitem discount",
    "Vendor"
]

# Keep only columns that exist
item_columns = [
    col for col in item_columns
    if col in df.columns
]

order_items = df[item_columns].copy()

# Rename columns
order_items = order_items.rename(columns={
    "Id": "order_id",
    "Lineitem name": "product_name",
    "Lineitem quantity": "quantity",
    "Lineitem price": "unit_price",
    "Lineitem compare at price": "compare_at_price",
    "Lineitem sku": "sku",
    "Lineitem requires shipping": "requires_shipping",
    "Lineitem taxable": "taxable",
    "Lineitem fulfillment status": "fulfillment_status",
    "Lineitem discount": "lineitem_discount",
    "Vendor": "vendor"
})

# Save order items
order_items_file = output_folder / "order_items.csv"
order_items.to_csv(order_items_file, index=False)


# ============================================================
# 2. CREATE ORDERS TABLE
# ============================================================

order_columns = [
    "Id",
    "Name",
    "Email",
    "Financial Status",
    "Paid at",
    "Fulfillment Status",
    "Fulfilled at",
    "Accepts Marketing",
    "Currency",
    "Subtotal",
    "Shipping",
    "Taxes",
    "Total",
    "Discount Code",
    "Discount Amount",
    "Shipping Method",
    "Created at",
    "Billing City",
    "Billing Province",
    "Billing Country",
    "Shipping City",
    "Shipping Province",
    "Shipping Country",
    "Cancelled at",
    "Payment Method",
    "Refunded Amount",
    "Outstanding Balance",
    "Location",
    "Source",
    "Risk Level"
]

# Keep only columns that exist
order_columns = [
    col for col in order_columns
    if col in df.columns
]

orders = df[order_columns].copy()

# One row per order
orders = orders.drop_duplicates(
    subset=["Id"],
    keep="first"
)

# Rename columns
orders = orders.rename(columns={
    "Id": "order_id",
    "Name": "customer_name",
    "Email": "email",
    "Financial Status": "financial_status",
    "Paid at": "paid_at",
    "Fulfillment Status": "fulfillment_status",
    "Fulfilled at": "fulfilled_at",
    "Accepts Marketing": "accepts_marketing",
    "Discount Code": "discount_code",
    "Discount Amount": "discount_amount",
    "Shipping Method": "shipping_method",
    "Created at": "created_at",
    "Billing City": "billing_city",
    "Billing Province": "billing_province",
    "Billing Country": "billing_country",
    "Shipping City": "shipping_city",
    "Shipping Province": "shipping_province",
    "Shipping Country": "shipping_country",
    "Cancelled at": "cancelled_at",
    "Payment Method": "payment_method",
    "Refunded Amount": "refunded_amount",
    "Outstanding Balance": "outstanding_balance",
    "Location": "location",
    "Source": "source",
    "Risk Level": "risk_level"
})

# Save orders
orders_file = output_folder / "orders.csv"
orders.to_csv(orders_file, index=False)


# ============================================================
# 3. SUMMARY
# ============================================================

print("\nSuccessfully created datasets!")

print("\nOrders:")
print("Rows:", len(orders))
print("Columns:", len(orders.columns))

print("\nOrder Items:")
print("Rows:", len(order_items))
print("Columns:", len(order_items.columns))

print("\nFiles created:")
print(orders_file)
print(order_items_file)