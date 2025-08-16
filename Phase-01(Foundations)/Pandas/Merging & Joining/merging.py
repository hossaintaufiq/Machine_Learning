import pandas as pd

df_customers= pd.DataFrame({
    "CustomerID": [1, 2, 3],
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [30, 40, 35]
})

df_orders = pd.DataFrame({
    "OrderID": [101, 102, 103],
    "CustomerID": [1, 2, 5],
    "Amount": [250, 150, 200]
})



# df_merged= pd.merge(df_customers,df_orders,on="CustomerID",how="outer")
# df_merged= pd.merge(df_customers,df_orders,on="CustomerID",how="inner")
# df_merged= pd.merge(df_customers,df_orders,on="CustomerID",how="left")
df_merged= pd.merge(df_customers,df_orders,on="CustomerID",how="right")
# df_merged= pd.merge(df_customers,df_orders,on="CustomerID",how="cross")
print('right join')
print(df_merged)