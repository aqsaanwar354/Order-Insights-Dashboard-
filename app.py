import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Page configuration
st.set_page_config(page_title="Order Insights Dashboard", page_icon="📊", layout="wide")

# Dashboard title
st.title("📊 Online Store - Order Insights")
st.write("Explore sales and order information.")

# Load cleaned dataset
df = pd.read_csv("data/orders_cleaned.csv")

# Total orders KPI
st.subheader("Key Performance Indicator")

total_orders = len(df)
st.metric("Total Orders", total_orders)

# Region filter
st.subheader("Filter Orders by Region")

regions = ["All"] + sorted(df["region"].dropna().unique().tolist())

selected_region = st.selectbox("Select Region", regions)

# Filter data
if selected_region == "All":
    filtered_df = df
else:
    filtered_df = df[df["region"] == selected_region]

# Sales chart

# Sales chart
st.subheader("Sales by Region")

sales_by_region = filtered_df.groupby("region")["order_value"].sum()

fig, ax = plt.subplots(figsize=(5, 3))

sales_by_region.plot(kind="bar", ax=ax, width=0.5)

ax.set_xlabel("Region", fontsize=9)
ax.set_ylabel("Total Sales", fontsize=9)
ax.set_title("Sales by Region", fontsize=11)
ax.tick_params(axis="both", labelsize=8)

plt.tight_layout()

st.pyplot(fig, use_container_width=False)
plt.close(fig)

# Display filtered orders
st.subheader("Order Details")

st.dataframe(filtered_df, use_container_width=True)

# Footer
st.success("Dashboard loaded successfully!")
