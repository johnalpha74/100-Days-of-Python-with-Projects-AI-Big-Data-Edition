"""
Author: John Alpha
Description: Bars Plots
Date: 02/09/25
Version: v001
"""

import matplotlib.pyplot as plt
import numpy as np

# Grouped bar plot: two series side-by-side
models = ['Model A', 'Model B', 'Model C']
acc_2024 = [0.82, 0.79, 0.85]
acc_2025 = [0.86, 0.83, 0.88]

xpos = np.arange(len(models))
width = 0.35  # bar width

plt.bar(xpos - width/2, acc_2024, width, label='2024')
plt.bar(xpos + width/2, acc_2025, width, label='2025')
plt.xticks(xpos, models)
plt.ylabel('Accuracy')
plt.title('Model Accuracy by Year')
plt.legend()
plt.show()
