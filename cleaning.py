import pandas as pd


# Function to clean orders
def clean_orders(df):

    # Create a copy of original dataset
    clean = df.copy()

    # Clean region and category
    clean["region"] = clean["region"].str.strip().str.title()
    clean["category"] = clean["category"].str.strip().str.title()

    # Convert order_date to datetime
    clean["order_date"] = pd.to_datetime(clean["order_date"], errors="coerce")

    # Convert columns to numeric
    for col in ["quantity", "unit_price", "order_value"]:
        clean[col] = pd.to_numeric(clean[col], errors="coerce")

    # Remove duplicate rows
    clean = clean.drop_duplicates()

    # Remove records missing essential details
    clean = clean.dropna(
        subset=[
            "order_id",
            "order_date",
            "region",
            "category",
            "quantity",
            "unit_price",
            "order_value",
            "status",
        ]
    )

    # Keep only positive values
    clean = clean[
        (clean["quantity"] > 0) & (clean["unit_price"] > 0) & (clean["order_value"] > 0)
    ]

    # Return cleaned dataset
    return clean


# Load original dataset
df = pd.read_csv("data/orders_raw.csv")

# Test the function
cleaned_df = clean_orders(df)

cleaned_df.to_csv("data/orders_cleaned.csv", index=False)
print("Cleaned dataset saved successfully!")

# Display results
print("Original Rows:", len(df))
print("Cleaned Rows:", len(cleaned_df))
print("Rows Removed:", len(df) - len(cleaned_df))

print("\nCleaned Data:")
print(cleaned_df.head())

print("\nMissing Values:")
print(cleaned_df.isnull().sum())


# Step 7: Create Data Quality Report

# Calculate row counts
rows_before = len(df)
rows_after = len(cleaned_df)
rows_removed = rows_before - rows_after

# Create report using dictionary
report = {
    "Metric": ["Rows Before Cleaning", "Rows After Cleaning", "Rows Removed"],
    "Count": [rows_before, rows_after, rows_removed],
}

# Convert dictionary into DataFrame
report_df = pd.DataFrame(report)

# Save report as CSV
report_df.to_csv("output/data_quality_report.csv", index=False)

print("\nData Quality Report:")
print(report_df)

print("\nReport saved successfully!")
