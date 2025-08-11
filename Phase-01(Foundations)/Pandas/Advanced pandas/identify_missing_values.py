import pandas as pd 

data={
    "Name": ["Alice", "Bob", "Charlie",None,"Charlie","Taufiq","Hossain","Sakib"],
    "Age": [25, 30, 35,None, 35, 23, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago",None, "Dhaka", "Dhaka", "Dhaka", "Dhaka"],
    "salary": [70000, 80000, 120000, None, 50000, 60000, 90000, 100000], 
    "Performance Score": [85, 90, 95, None, 75, 88, 92, 89]
}

df= pd.DataFrame(data)

print(df.isnull())  # Check for missing values
print(df.isnull().sum())  # Count of missing values in each column