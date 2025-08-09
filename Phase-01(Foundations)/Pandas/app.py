import pandas as pd 

#read data from csv file 

# df = pd.read_csv('sales_data_sample.csv', encoding='latin1')

# print(df)


#read from excel file 

# df_excel = pd.read_excel('SampleSuperstore.xlsx')

# print(df_excel)


#read from json file 

df_json= pd.read_json('sample_Data.json')

print(df_json) 