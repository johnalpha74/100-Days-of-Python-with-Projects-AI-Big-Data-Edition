"""
Author: John Alpha
Description: Histograms
Date: 02/09/25
Version: v001
"""

import matplotlib.pyplot as plt
import numpy as np

# Synthetic data: normally distributed feature
data = np.random.normal(loc=50, scale=10, size=500)

plt.hist(data, bins=20, edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram: Synthetic Feature Distribution')
plt.show()
