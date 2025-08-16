import pandas as pd

data= {
    "Name": ["Alice", "Bob", "Charlie","Arun","Barun"],
    "Age": [40, 45,40 , 50, 45],
    "Salary": [70000, 80000, 90000, 60000, 100000]
}

df=pd.DataFrame(data)

print("Original DataFrame:")
print(df)

# grouped = df.groupby("Age")["Salary"].sum()
grouped = df.groupby(["Age","Name"])["Salary"].max()
print(grouped)