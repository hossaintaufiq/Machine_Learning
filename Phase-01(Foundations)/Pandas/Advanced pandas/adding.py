import pandas as pd 

data={
    "Name": ["Alice", "Bob", "Charlie","Taufiq","Charlie","Taufiq","Hossain","Sakib"],
    "Age": [25, 30, 35,23, 35, 23, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago","Dhaka", "Dhaka", "Dhaka", "Dhaka", "Dhaka"],
    "salary": [70000, 80000, 120000, 50000, 50000, 60000, 90000, 100000], 
    "Performance Score": [85, 90, 95, 80, 75, 88, 92, 89]
}

df= pd.DataFrame(data)

# square brackets df["column_name"] to access a column = some data 

df["Bonus"]= df["salary"]*.1 
# print(df)


# using insert method to add a new column at a specific position

df.insert(5, "Experience", [2, 5, 10, 1, 3, 4, 8, 6])

df.insert(0, "Employee ID", range(1, len(df) + 1))
print(df)
df.to_csv("employee_data.csv",index=False)