import pandas as pd

data= {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
    }

df= pd.DataFrame(data)
print(df)

#save to CSV file 
df.to_csv("output.csv", index=False)


#save to Excel file 

df.to_excel("output.xlsx", index=False)


#save to Json file 

df.to_json("output.json")
