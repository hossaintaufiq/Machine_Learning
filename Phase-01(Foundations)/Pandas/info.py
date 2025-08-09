import pandas as pd 

# df= pd.read_json("sample_Data.json")

data= {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
    }

df= pd.DataFrame(data)

print("Dispaly the info of the DataFrame:")

#df.info() is a method that provides a concise summary of the DataFrame, including the number of non-null entries, data types, and memory usage.
print(df.info())

