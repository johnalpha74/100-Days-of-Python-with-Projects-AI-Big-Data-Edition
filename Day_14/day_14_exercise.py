"""
using day14_sales.csv with synthetic data:

Line: Plot monthly revenue over month.
Bar: Total revenue by region.
Histogram: Distribution of units sold.
"""

import matplotlib.pyplot as plt
import pandas as pd
# Load the exercise CSV
sales = pd.read_csv(r"day14_sales.csv")
sales.head()

# Line — revenue over month
plt.plot(sales['month'], sales['revenue'], marker='o')
plt.xlabel('Month')
plt.ylabel('Revenue')
plt.title('Revenue Over Time')
plt.show()

# Bar — total revenue by region
grp = sales.groupby('region')['revenue'].sum()
plt.bar(grp.index, grp.values)
plt.xlabel('Region')
plt.ylabel('Total Revenue')
plt.title('Total Revenue by Region')
plt.show()

# Histogram — units
plt.hist(sales['units'], bins=10, edgecolor='black')
plt.xlabel('Units')
plt.ylabel('Frequency')
plt.title('Distribution of Units Sold')
plt.show()
