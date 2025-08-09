import pandas as pd

data={
    "Name": ["Alice", "Bob", "Charlie","Taufiq","Charlie","Taufiq","Hossain","Sakib"],
    "Age": [25, 30, 35,23, 35, 23, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago","Dhaka", "Dhaka", "Dhaka", "Dhaka", "Dhaka"],
    "salary": [70000, 80000, 120000, 50000, 50000, 60000, 90000, 100000], 
    "Performance Score": [85, 90, 95, 80, 75, 88, 92, 89]
}

df=pd.DataFrame(data)

# Selecting columns 

# Selecting a single column
# name= df["Name"]
# print(name)

# selecting multiple columns

# multiple_columns = df[["Name", "Age", "City"]] #2d array cz it returns a DataFrame 
# print(multiple_columns)


# selecting rows based on conditions 

# selecting based on a single condition 
limited_salary = df[df["salary"]>50000]

# print(limited_salary)


# selecting rows based on a multiple conditions 

# high_performance = df[(df["Performance Score"]>85)& (df["salary"]>60000)]

# using or operator 
high_performance = df[(df["Performance Score"]>85)|(df["salary"]>60000)]
print(high_performance)
print(high_performance.describe())
print("Infor method for the hight_performance DataFrame: ")
print(high_performance.info())