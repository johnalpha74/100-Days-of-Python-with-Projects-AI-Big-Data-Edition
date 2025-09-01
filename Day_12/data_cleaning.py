# Day 12 Mini-Project Setup: Handling Missing Data & Cleaning in Pandas


# Load CSV into Pandas
import pandas as pd
df = pd.read_csv("empoyees.csv")
print(df)

# Detect Missing Data
print(df.isna().sum())  # Count NaNs per column

# Drop Missing Data
df_drop = df.dropna() # Drop rows with any NaN

# Fill Missing Data
df['Age'] = df['Age'].fillna((df['Age']).median())       # Fill Age with median
df['Salary'] = df['Salary'].fillna((df['Salary']).mean())   # Fill Salary with mean
df['Department'] = df['Department'].fillna(df['Department']).mode()      # Fill Department with mode

# Forward/Backward Fill
df_ffill = df.fillna(method='ffill')
df_bfill = df.fillna(method='bfill')

# Interpolation
df.interp = df.interpolate(method='linear')

# Final Cleaned Dataset
print(df)
df.to_csv("employees_cleaned.csv", index=False)


