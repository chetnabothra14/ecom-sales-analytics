import pandas as pd
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
cleaned_folder = project_root / "data" / "cleaned"

orders_file = cleaned_folder / "orders_cleaned.csv"
output_file = cleaned_folder / "orders_anonymized.csv"

orders = pd.read_csv(orders_file)

print("Loaded orders:", len(orders))

# Keep track of customers using ONLY real email addresses
valid_email = (
    orders["email"].notna()
    & (orders["email"].str.strip() != "")
    & (orders["email"] != "Not Available")
)

customer_map = {}

customer_counter = 1

for index, row in orders.iterrows():

    email = row["email"]

    if valid_email.loc[index]:
        # Same email = same customer
        if email not in customer_map:
            customer_map[email] = f"Customer_{customer_counter:03d}"
            customer_counter += 1

        orders.loc[index, "customer_id"] = customer_map[email]

    else:
        # No email = cannot reliably identify the customer
        orders.loc[index, "customer_id"] = (
            f"Customer_{customer_counter:03d}"
        )
        customer_counter += 1

# Anonymize name
orders["customer_name"] = orders["customer_id"]

# Keep missing emails as NULL
orders["email"] = orders["email"].replace(
    "Not Available",
    pd.NA
)

# Remove phone if it exists
if "phone" in orders.columns:
    orders["phone"] = pd.NA

orders.to_csv(
    output_file,
    index=False
)

print("\nAnonymization completed!")
print("Orders:", len(orders))
print("Unique customers:", orders["customer_id"].nunique())

print("\nMissing emails:",
      orders["email"].isna().sum())

print("\nCreated:")
print(output_file)