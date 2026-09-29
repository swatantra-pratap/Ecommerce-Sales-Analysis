import pandas as pd
import matplotlib.pyplot as plt

RAW_FILE = "data/raw/ecommerce_sales.csv"
PROCESSED_FILE = "data/processed/cleaned_sales.csv"

# Load
df = pd.read_csv(RAW_FILE)

# Clean
df = df.drop_duplicates()
df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
df["region"] = df["region"].fillna("Unknown")
df["payment_method"] = df["payment_method"].fillna("Unknown")
df["discount_pct"] = df["discount_pct"].fillna(df["discount_pct"].median())
df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce").fillna(0)
df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0).astype(int)
df["month"] = df["order_date"].dt.to_period("M").astype(str)

df.to_csv(PROCESSED_FILE, index=False)

# KPI analysis
completed = df[df["order_status"] == "Completed"].copy()
total_revenue = completed["revenue"].sum()
total_orders = completed["order_id"].nunique()
aov = total_revenue / total_orders

print(f"Total Revenue: ₹{total_revenue:,.2f}")
print(f"Completed Orders: {total_orders:,}")
print(f"Average Order Value: ₹{aov:,.2f}")
print(f"Unique Customers: {completed['customer_id'].nunique():,}")

# Monthly revenue
monthly = completed.groupby("month")["revenue"].sum()
monthly.plot(kind="line", marker="o", figsize=(10,5), title="Monthly Revenue")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Category performance
category = completed.groupby("category")["revenue"].sum().sort_values(ascending=False)
print("\nRevenue by Category:")
print(category)

# Top products
top_products = completed.groupby("product")["revenue"].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products:")
print(top_products)
