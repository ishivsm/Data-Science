"""
vertically(row_wise)--0
horizontally (column wise)--1
pd.concatane([df1,df2],axis=0,ignore_index=True)
ignorede_index-= true
"""

import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul"],
    "Age": [25, 30, 28],
    "Salary": [45000, 60000, 55000]
})

df2 = pd.DataFrame({
    "Name": ["Sneha", "Vijay", "Neha"],
    "Age": [24, 35, 29],
    "Salary": [35000, 70000, 60000]
})

print(df1)
print(df2)




result = pd.concat([df1, df2], axis=0)

print(result)       


result = pd.concat(
    [df1, df2],
    ignore_index=True
)

print(result)


df3 = pd.DataFrame({
    "City": ["Pune", "Mumbai", "Delhi"],
    "Department": ["IT", "HR", "Sales"]
})


result = pd.concat(
    [df1, df3],
    axis=1
)

print(result)