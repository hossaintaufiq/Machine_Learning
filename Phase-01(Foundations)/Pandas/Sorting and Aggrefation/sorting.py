""" 
Sorting data 
-Sorting data in 1 column
df = pd.DataFrame({
    'A': [3, 2, 1],
    'B': ['c', 'b', 'a']
})

df.sort_values(by='A', inplace=True)

"""

import pandas as pd

data= {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [40, 45, 35 ],
    "Salary": [70000, 80000, 90000]
}

df=pd.DataFrame(data)

print("Original DataFrame:")
print(df)


# print("\nSorting by Age in descending order:")

# df.sort_values(by='Age', ascending=False,inplace=True)
# print(df)


print("\nSorting by Age in ascending order:")
df.sort_values(by='Age', ascending=True, inplace=True)
print(df)