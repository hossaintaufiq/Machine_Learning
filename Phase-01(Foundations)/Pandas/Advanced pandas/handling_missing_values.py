import pandas as pd 

data={
    "Name": ["Alice", "Bob", "Charlie",None,"Charlie","Taufiq","Hossain","Sakib"],
    "Age": [25, 30, 35,None, 35, 23, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago",None, "Dhaka", "Dhaka", "Dhaka", "Dhaka"],
    "salary": [70000, 80000, 120000, None, 50000, 60000, 90000, 100000], 
    "Performance Score": [85, 90, 95, None, 75, 88, 92, 89]
}

df= pd.DataFrame(data)
print(df)

print("After Handling Missing Values:")

# df.dropna(inplace = True) # Drop rows with any missing values
# print(df)

# df.fillna(0, inplace=True)  # Fill missing values with 0

df['Age'].fillna(df['Age'].mean(), inplace=True)  # Fill missing Age with mean
df['salary'].fillna(df['salary'].mean(),inplace=True)  # Fill missing salary with mean
df['Performance Score'].fillna(df['Performance Score'].mean(), inplace=True)  # Fill missing Performance Score with mean
# print(df.isnull())
df.fillna(0,inplace=True)
print(df)