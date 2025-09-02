"""
Author: John Alpha
Description: Day 14 — Matplotlib Basic
DAte: 02/09/255
Version: V01

"""

import matplotlib.pyplot as plt
import numpy as np

# For reproducibility
np.random.seed(42)

# Trend over time (synthetic series)
x = np.arange(1, 13)  # months
y = np.array([12, 15, 14, 18, 20, 22, 21, 24, 23, 25, 27, 30])

plt.plot(x, y, marker='o', label='Monthly value')
plt.xlabel('Month')
plt.ylabel('Value')
plt.title('Line Chart Example')
plt.legend()
plt.show()

x = np.arange(1, 13)  # months
y = np.array([12, 15, 14, 18, 20, 22, 21, 24, 23, 25, 27, 30])

# Overlay two lines (e.g., plan vs actual). Multiple plt.plot calls before show.
plt.plot(x, y, marker='o', label='Monthly value')
plt.xlabel('Month')
plt.ylabel('Value')
plt.title('Line Chart Example')
plt.legend()
plt.show()
