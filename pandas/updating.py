import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahul", "Amit", "Priya", "Sneha", "Rohan"],
    "Age": [22, 25, 24, 28, 23],
    "City": ["Pune", "Mumbai", "Delhi", "Pune", "Nashik"],
    "Salary": [30000, 45000, 40000, 60000, 35000]
})
df=pd.DataFrame(df)
print(df)
#.loc[]#df.loc[row_index,"column_nname"]=new_value

df.loc[0,"Salary"]=55000
print(df)   
#increasing salary 
df["Salary"]=df["Salary"]*1.05
print(df)