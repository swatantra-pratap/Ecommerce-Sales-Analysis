"""
E-commerce Sales Analysis
End-to-end Python data cleaning, EDA, KPI analysis and business insights.

This version is designed for the current GitHub repository structure,
where the CSV and Python files are in the repository root.
"""

import pandas as pd
import matplotlib.pyplot as plt

RAW_FILE = "ecommerce_sales.csv"
CLEAN_FILE = "cleaned_sales.csv"


def load_and_clean_data():
    df = pd.read_csv(RAW_FILE)

    print("----- DATA QUALITY CHECK -----")
    print(f"Rows before cleaning: {len(df):,}")
    print(f"Duplicate rows: {df.duplicated().sum():,}")
    print("\nMissing values:")
    print(df.isna().sum())

    df = df.drop_duplicates().copy()
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
    df["region"] = df["region"].fillna("Unknown")
    df["payment_method"] = df["payment_method"].fillna("Unknown")
    df["discount_pct"] = df["discount_pct"].fillna(df["discount_pct"].median())
    df["revenue"] = pd.to_numeric(df["revenue"], errors="coerce").fillna(0)
    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce").fillna(0).astype(int)
    df["month"] = df["order_date"].dt.to_period("M").astype(str)

    df.to_csv(CLEAN_FILE, index=False)
    print(f"Rows after cleaning: {len(df):,}")

    return df


def analyze(df):
    completed = df[df["order_status"] == "Completed"].copy()

    total_revenue = completed["revenue"].sum()
    total_orders = completed["order_id"].nunique()
    unique_customers = completed["customer_id"].nunique()
    total_units = completed["quantity"].sum()
    aov = total_revenue / total_orders

    cancelled_pct = (df["order_status"] == "Cancelled").mean() * 100
    returned_pct = (df["order_status"] == "Returned").mean() * 100

    print("\n----- BUSINESS KPIs -----")
    print(f"Total Revenue: ₹{total_revenue:,.2f}")
    print(f"Completed Orders: {total_orders:,}")
    print(f"Unique Customers: {unique_customers:,}")
    print(f"Units Sold: {total_units:,}")
    print(f"Average Order Value: ₹{aov:,.2f}")
    print(f"Cancellation Rate: {cancelled_pct:.2f}%")
    print(f"Return Rate: {returned_pct:.2f}%")

    monthly = (
        completed.groupby("month", as_index=False)
        .agg(revenue=("revenue", "sum"),
             orders=("order_id", "nunique"),
             units=("quantity", "sum"))
    )
    monthly["mom_growth_pct"] = monthly["revenue"].pct_change() * 100

    category = (
        completed.groupby("category", as_index=False)
        .agg(revenue=("revenue", "sum"),
             orders=("order_id", "nunique"),
             units=("quantity", "sum"))
        .sort_values("revenue", ascending=False)
    )
    category["revenue_share_pct"] = (
        category["revenue"] / category["revenue"].sum() * 100
    )

    region = (
        completed.groupby("region", as_index=False)
        .agg(revenue=("revenue", "sum"),
             orders=("order_id", "nunique"))
        .sort_values("revenue", ascending=False)
    )

    channel = (
        completed.groupby("channel", as_index=False)
        .agg(revenue=("revenue", "sum"),
             orders=("order_id", "nunique"),
             units=("quantity", "sum"))
    )
    channel["aov"] = channel["revenue"] / channel["orders"]
    channel = channel.sort_values("revenue", ascending=False)

    product = (
        completed.groupby("product", as_index=False)["revenue"]
        .sum()
        .sort_values("revenue", ascending=False)
        .head(10)
    )

    print("\n----- CATEGORY PERFORMANCE -----")
    print(category.to_string(index=False))

    print("\n----- REGION PERFORMANCE -----")
    print(region.to_string(index=False))

    print("\n----- CHANNEL PERFORMANCE -----")
    print(channel.to_string(index=False))

    print("\n----- TOP 10 PRODUCTS -----")
    print(product.to_string(index=False))

    return monthly, category, region, channel, product


if __name__ == "__main__":
    data = load_and_clean_data()
    analyze(data)
