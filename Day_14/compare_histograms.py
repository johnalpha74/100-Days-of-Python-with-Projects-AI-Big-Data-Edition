import matplotlib.pyplot as plt
import numpy as np

# Compare two distributions by overlaying two hist calls with transparency
d1 = np.random.normal(50, 10, 500)
d2 = np.random.normal(60, 8, 500)

plt.hist(d1, bins=20, alpha=0.5, label='Group 1')
plt.hist(d2, bins=20, alpha=0.5, label='Group 2')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram: Comparing Two Groups')
plt.legend()
plt.show()
