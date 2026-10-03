import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahul", "Amit", "Priya", "Sneha", "Rohan"],
    "Age": [22, 25, 24, 28, 23],
    "City": ["Pune", "Mumbai", "Delhi", "Pune", "Nashik"],
    "Salary": [30000, 45000, 40000, 60000, 35000]
})
df=pd.DataFrame(df)

#df.drop(column_name)=["Columnsname"],inplace=True

df.drop(columns=["City"],inplace=True)
print(df)

df=df.drop("Name",axis=1)
print(df)

df=df.drop(["Age","Salary"],axis=1)
print(df)