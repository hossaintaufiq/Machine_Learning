import pandas as pd 

df=pd.read_json("sample_Data.json")

print("Display 10 1st rows of the dataset")

head=df.head(10)
print(head)
print("Display 10 last rows of the dataset")

tail=df.tail(10)
print(tail)