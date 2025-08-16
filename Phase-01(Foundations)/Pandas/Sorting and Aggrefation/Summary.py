"""
df["column name"].mean()
df["column name"].median()
df["Column_name"].sum()
df["Column_name"].min()
df["column_name"].max()
etc
"""

import pandas as pd

data= {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [40, 45, 35 ],
    "Salary": [70000, 80000, 90000]
}

df=pd.DataFrame(data)

print("Original DataFrame:")
print(df)

avg_salary=df["Age"].mean()
max_salary=df["Salary"].max()
min_age=df["Age"].min()
min_salary=df["Salary"].min()
sum_age=df["Age"].sum()

print("\nAverage Age:", avg_salary)
print("Maximum Salary:", max_salary)
print("Minimum Age:", min_age)
print("Minimum Salary:", min_salary)
print("Sum of Ages:", sum_age)