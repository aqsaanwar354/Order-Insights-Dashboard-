import pandas as pd

# Load the cleaned dataset
df = pd.read_csv("data/orders_cleaned.csv")

# Mean, Median and Standard Deviation
print("Mean Order Value:")
print(df["order_value"].mean())

print("\nMedian Order Value:")
print(df["order_value"].median())

print("\nStandard Deviation:")
print(df["order_value"].std())

# Sales by Region
sales_by_region = df.groupby("region")["order_value"].sum()
print("\nSales by Region:")
print(sales_by_region)

# Category Counts
category_counts = df["category"].value_counts()
print("\nCategory Counts:")
print(category_counts)

# Region vs Category
region_category = pd.crosstab(df["region"], df["category"])
print("\nRegion vs Category:")
print(region_category)
