import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahul", "Amit", "Priya", "Sneha", "Rohan"],
    "Age": [22, 25, 24, 28, 23],
    "City": ["Pune", "Mumbai", "Delhi", "Pune", "Nashik"],
    "Salary": [30000, 45000, 40000, 60000, 35000]
})

df=pd.DataFrame(df)
print(df)


#selecting
print("Name single columns")
print(df["Name"])

#or

name=df["Name"]
print(name)

#selecting multiple columns
suubset=df[["Name","Age","City"]]
print(suubset)