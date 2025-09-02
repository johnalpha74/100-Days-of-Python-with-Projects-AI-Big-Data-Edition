"""
Author: John Alpha
Descrption: Bar Plots
Date: 02/09/25
Version:vo01
"""

import matplotlib.pyplot as plt
import numpy as np

# Bar Plots — plt.bar()
categories = ['North', 'South', 'East', 'West']
values = [120, 150, 100, 130]

plt.bar(categories, values)
plt.xlabel('Region')
plt.ylabel('Sales (k)')
plt.title('Bar Plot: Sales by Region')
plt.show()
