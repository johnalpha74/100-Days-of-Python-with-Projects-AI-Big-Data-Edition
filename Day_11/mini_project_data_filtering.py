import pandas as pd

df = pd.read_csv("employees.csv")

print("Dataset shape:", df.shape)
df.head()

# Select employees with salary > 70000
high_salary = df.loc[df['Salary'] > 70000, ["EmployeeID", "Name", "Department", "Salary"]]

print("Employees with salary above 70k:")
print(high_salary.head(10))

# Grab first 5 rows using iloc
first_rows = df.iloc[:5, :]
print("First 5 employees:\n", first_rows)

# Example: Age > 30, Department = 'IT', Salary > 60000
subset = df.loc[
    (df['Age'] > 30) &
    (df['Department'] == "IT") &
    (df['Salary'] > 60000),
    ["EmployeeID", "Name", "Age", "Department", "Salary"]
]

print("Filtered subset:\n", subset)

# Save results of subset for sharing
subset.to_csv("filtered_employees.csv", index=False)
print("Filtered data exported to filtered_employees.csv")
