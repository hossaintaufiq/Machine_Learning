# based on mathmatical interpolation methods

import pandas as pd 



data={
    "Name": ["Alice", "Bob", "Charlie",None,"Charlie","Taufiq","Hossain","Sakib"],
    "Age": [25, 30, 35,None, 35, 23, 40, 45],
    "City": ["New York", "Los Angeles", "Chicago",None, "Dhaka", "Dhaka", "Dhaka", "Dhaka"],
    "salary": [70000, 80000, 120000, None, 50000, 60000, 90000, 100000], 
    "Performance Score": [85, 90, 95, None, 75, 88, 92, 89]
}

df= pd.DataFrame(data)

df.interpolate(method='linear',axis=0, inplace=True)  # Linear interpolation for numerical columns
# Linear , polynomial , time method 