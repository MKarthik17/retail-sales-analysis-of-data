import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load and clean
df = pd.read_csv("data/superstore.csv", encoding="latin-1")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_").str.replace("-", "_")
df["order_date"] = pd.to_datetime(df["order_date"])
df = df.drop_duplicates()
df["month"] = df["order_date"].dt.to_period("M").astype(str)
df["profit_margin"] = df["profit"] / df["sales"]

# 2. Key metrics
print("Total sales:", round(df["sales"].sum(), 2))
print("Total profit:", round(df["profit"].sum(), 2))
print("Overall margin:", round(df["profit"].sum() / df["sales"].sum() * 100, 2), "%")

# 3. Monthly sales trend
monthly = df.groupby("month")["sales"].sum()
monthly.plot(figsize=(10, 4), title="Monthly Sales Trend")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.clf()

# 4. Profit by category and sub-category
sub = df.groupby(["category", "sub_category"])["profit"].sum().sort_values()
sub.plot(kind="barh", figsize=(8, 8), title="Profit by Sub-Category")
plt.tight_layout()
plt.savefig("profit_by_subcategory.png")
plt.clf()

# 5. Discount vs profit
print(df.groupby(pd.cut(df["discount"], [-0.01, 0, 0.2, 0.4, 1]), observed=True)["profit"].mean())

# 6. Run SQL on the same data
conn = sqlite3.connect(":memory:")
df.to_sql("orders", conn, index=False)
with open("queries.sql") as f:
    for q in f.read().split(";"):
        if q.strip():
            print(pd.read_sql(q, conn), "\n")
