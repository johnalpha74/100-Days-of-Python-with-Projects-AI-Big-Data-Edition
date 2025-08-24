# Day 11 - Data Selection & Indexing

import pandas as pd

# Sample DataFrame
data = {
    "name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "age": [24, 30, 22, 35, 28],
    "salary": [5000, 6000, 4500, 8000, 7000],
    "gender": ["F", "M", "M", "M", "F"]
}
df = pd.DataFrame(data, index=[101, 102, 103, 104, 105])
print("DataFrame:\n", df)

# 1. loc - label-based
print("\nRow with index 101:\n", df.loc[101])
print("\nAll ages:\n", df.loc[:, "age"])

# 2. iloc - integer-based
print("\nFirst row:\n", df.iloc[0])
print("\nFirst two rows and cols:\n", df.iloc[:2, :2])

# 3. Filters
print("\nSalary > 6000:\n", df.loc[df['salary'] > 6000])

# 4. Multiple conditions
print("\nAge > 25 AND gender=F:\n", df.loc[(df['age'] > 25) & (df['gender'] == 'F')])

# 5. Slicing
print("\nSubset rows 101-103, cols age-salary:\n", df.loc[101:103, "age":"salary"])
