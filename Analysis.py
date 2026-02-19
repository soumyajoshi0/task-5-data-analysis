# Task 5 - CSV Data Analysis

import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv("sales.csv")
print("First 5 rows:")
print(df.head())

# Total sales by product
print("\nTotal sales by product:")
product_sales = df.groupby("Product")["Sales"].sum()
print(product_sales)

# Total sales by region
print("\nTotal sales by region:")
region_sales = df.groupby("Region")["Sales"].sum()
print(region_sales)

# Plot chart
product_sales.plot(kind="bar", title="Sales by Product")
plt.xlabel("Product")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()
