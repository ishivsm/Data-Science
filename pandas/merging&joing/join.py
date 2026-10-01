import pandas as pd

df1 = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul"],
    "Salary": [40000, 50000, 60000]
}, index=[1, 2, 3])

df2 = pd.DataFrame({
    "Department": ["IT", "HR", "Sales"],
    "City": ["Pune", "Mumbai", "Delhi"]
}, index=[1, 2, 3])

result = df1.join(df2)

print(result)


df1 = pd.DataFrame({
    "Name": ["Amit", "Priya", "Rahul"]
}, index=[1, 2, 3])

df2 = pd.DataFrame({
    "Salary": [40000, 50000, 60000]
}, index=[1, 2, 4])

print(df1.join(df2))

#how parameter

df1.join(df2, how="left")

df1.join(df2, how="right")

df1.join(df2, how="inner")

df1.join(df2, how="outer")


"""
| `how`   | Meaning                     |
| ------- | --------------------------- |
| `left`  | Keep all indexes from `df1` |
| `right` | Keep all indexes from `df2` |
| `inner` | Keep only matching indexes  |
| `outer` | Keep all indexes from both  |


"""