# Day 8 – Environment Setup and First Steps with NumPy, Pandas, Matplotlib

# 1. Check installations and versions
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

print("NumPy version:", np.__version__)
print("Pandas version:", pd.__version__)
print("Matplotlib version:", matplotlib.__version__)

# 2. NumPy – create and manipulate arrays
arr = np.array([1, 2, 3, 4, 5])
print("\nNumPy Array:", arr)
print("Array mean:", np.mean(arr))
print("Array squared:", arr**2)

# 3. Pandas – create a simple DataFrame
data = {
    "Name": ["Alice", "Bob", "Charlie", "David"],
    "Age": [24, 27, 22, 32],
    "Score": [85, 90, 88, 95]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:\n", df)

print("\nStatistical Summary:\n", df.describe())

# 4. Matplotlib – basic plot
x = np.linspace(0, 10, 100)
y = np.sin(x)

plt.plot(x, y, label="Sine Wave")
plt.title("Day 8 – First Matplotlib Plot")
plt.xlabel("x")
plt.ylabel("sin(x)")
plt.legend()
plt.show()
