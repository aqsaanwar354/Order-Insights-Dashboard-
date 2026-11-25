import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("data/orders_cleaned.csv")

# 1. Histogram of Order Values
plt.figure(figsize=(8, 5))
plt.hist(df["order_value"], bins=20)
plt.title("Distribution of Order Values")
plt.xlabel("Order Value")
plt.ylabel("Frequency")
plt.savefig("output/order_value_histogram.png")
plt.show()

# 2. Bar Chart: Sales by Region
sales_by_region = df.groupby("region")["order_value"].sum()

plt.figure(figsize=(8, 5))
sales_by_region.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.savefig("output/sales_by_region.png")
plt.show()

# 3. Scatter Plot: Order Value vs Delivery Days
plt.figure(figsize=(8, 5))
plt.scatter(df["delivery_days"], df["order_value"])
plt.title("Order Value vs Delivery Days")
plt.xlabel("Delivery Days")
plt.ylabel("Order Value")
plt.savefig("output/order_vs_delivery.png")
plt.show()

print("All graphs saved successfully!")
