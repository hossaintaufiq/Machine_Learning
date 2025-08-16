import pandas as pd

data= {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [40, 45, 35 ],
    "Salary": [70000, 80000, 90000]
}

df=pd.DataFrame(data)

print("Original DataFrame:")
print(df)

df.sort_values(by=["Age","Salary"], ascending=[True, False], inplace=True)
print("\nDataFrame after sorting by Age (ascending) and Salary (descending):")
print(df)