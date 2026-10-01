import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahul", "Amit", "Priya", "Sneha", "Rohan"],
    "Age": [22, 25, 24, 28, 23],
    "City": ["Pune", "Mumbai", "Delhi", "Pune", "Nashik"],
    "Salary": [30000, 45000, 40000, 60000, 35000]
})
df=pd.DataFrame(df)
print(df)

#square brackets df["column_nbame"]=value

df["Bonus"]=df["Salary"]*0.1
print(df)

#using insert method  #insert()
#df.insert(loc."column_name",some_data)
df.insert(3,"Performance_score",[10,20,30,40,50])
print(df)