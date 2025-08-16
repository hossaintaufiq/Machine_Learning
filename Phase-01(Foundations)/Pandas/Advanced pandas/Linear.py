import pandas as pd 

data={
    "time": [1,2,3,4,5,6],
    "value": [10, None, 30, None, 50, 60]
    }

df=pd.DataFrame(data)

print("Before Interpolation")

print(df)

print("After Interpolation")

df.interpolate(method='linear', inplace=True)

print(df)


"""
use case 
    1-timer series data 
    2-numeric data with trends 
    3-avoid dropping rows 
    4- can't use in catagorical data 
    5-sometimes the interpolation calculation doesn't work as expected

"""