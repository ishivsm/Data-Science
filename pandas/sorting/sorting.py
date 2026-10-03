#sorting data
#sorting data 1 column sort_vqalues()
#df.sort_values(by="column name",True/False,inplace=True)

import pandas as pd

df = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 110],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Vijay",
             "Neha", "Akash", "Pooja", "Rohit", "Anjali"],
    "Department": ["IT", "HR", "IT", "Sales", "HR",
                   "IT", "Sales", "Finance", "IT", "Finance"],
    "City": ["Pune", "Mumbai", "Pune", "Delhi", "Mumbai",
             "Pune", "Delhi", "Mumbai", "Delhi", "Pune"],
    "Age": [25, 32, 28, 24, 35, 29, 26, 31, 27, 30],
    "Salary": [45000, 65000, 55000, 35000, 70000,
               60000, 40000, 75000, 50000, 68000],
    "Experience": [2, 7, 4, 1, 9, 5, 3, 8, 4, 6]
})

#single
df.sort_values(by=["City"],ascending=True,inplace=True)
print(df)


print()
#multi
df.sort_values(by=["City","Age"]
               ,ascending=[False,True],inplace=True)
print(df)