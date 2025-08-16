"""
joining data in 
-vertically(row-wise)
-horizontally(column-wise)

pd.concat([df1, df2], axis=0)  # Vertical concatenation
pd.concat([df1, df2], axis=1)  # Horizontal concatenation
"""

import pandas as pd

df_customers= pd.DataFrame({
    "CustomerID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 40, 35]
})

print(df_customers)
df_orders = pd.DataFrame({
    "OrderID": [101, 102, 103],
    "CustomerID": [1, 2, 3],
    "Amount": [250, 150, 200]
})
print(df_orders)


vertical=pd.concat([df_customers, df_orders], axis=0)  # Vertical concatenation
horizontal=pd.concat([df_customers, df_orders], axis=1)  # Horizontal concatenation


print("Vertical Concatenation:")
print(vertical)

print("\nHorizontal Concatenation:")
print(horizontal)   