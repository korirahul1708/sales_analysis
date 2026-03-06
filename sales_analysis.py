import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset

df = pd.read_csv("sales_dataset_5000_rows.csv")

print("First 5 rows of dataset:")
print(df.head())


# Create Revenue Column

df["revenue"] = df["quantity"] * df["price"]

print("\nTotal Revenue:")
print(df["revenue"].sum())


# Top Selling Products

top_products = df.groupby("product")["quantity"].sum().sort_values(ascending=False)

print("\nTop Selling Products:")
print(top_products)

plt.figure(figsize=(8,5))
top_products.plot(kind="bar")
plt.title("Top Selling Products")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top_products.png")
plt.show()


# Revenue by City

city_sales = df.groupby("city")["revenue"].sum().sort_values(ascending=False)

print("\nRevenue by City:")
print(city_sales)

plt.figure(figsize=(8,5))
city_sales.plot(kind="bar", color="orange")
plt.title("Revenue by City")
plt.xlabel("City")
plt.ylabel("Revenue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("city_sales.png")
plt.show()


# Monthly Sales Trend

df["date"] = pd.to_datetime(df["date"])

monthly_sales = df.groupby(df["date"].dt.month)["revenue"].sum()

print("\nMonthly Sales:")
print(monthly_sales)

plt.figure(figsize=(8,5))
monthly_sales.plot(kind="line", marker="o")
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.show()

print("\nAnalysis completed successfully!")