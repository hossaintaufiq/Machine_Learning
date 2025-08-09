import pandas as pd

data={
    "Name": ["Alice", "Bob", "Charlie","Taufiq","Charlie","Taufiq","Hossain","Sakib"],
    "Age": [25, 30, 35,23, 35, 23, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago","Dhaka", "Dhaka", "Dhaka", "Dhaka", "Dhaka"],
    "salary": [70000, 80000, 120000, 50000, 50000, 60000, 90000, 100000], 
    "Performance Score": [85, 90, 95, 80, 75, 88, 92, 89]
}

df=pd.DataFrame(data)

print(df)

print("Display the description of the DataFrame:")
print(df.describe())