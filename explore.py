import pandas as pd

# Load dataset
df = pd.read_csv("data/orders_raw.csv")

# Display first five rows
print("First Five Rows:")
print(df.head())

# Display dataset shape
print("\nDataset Shape:")
print(df.shape)

# Display column names
print("\nColumn Names:")
print(df.columns)

# Display data types
print("\nData Types:")
print(df.dtypes)

# Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Display unique regions
print("\nUnique Regions:")
print(df["region"].unique())

# Display unique categories
print("\nUnique Categories:")
print(df["category"].unique())
