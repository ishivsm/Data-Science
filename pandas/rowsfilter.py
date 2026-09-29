import pandas as pd

df = pd.DataFrame({
    "Name": ["Rahul", "Amit", "Priya", "Sneha", "Rohan"],
    "Age": [22, 25, 24, 28, 23],
    "City": ["Pune", "Mumbai", "Delhi", "Pune", "Nashik"],
    "Salary": [30000, 45000, 40000, 60000, 35000]
})

df=pd.DataFrame(df)
print(df)
#single filtering

high_salary=df[df['Salary']>50000]
print(high_salary)

#multiple condition filtering rows salary>50 &age >38

mul=df[(df["Age"]>25)&(df["Salary"]>40000)]
print(mul)

mule=df[(df["Age"]>25)|(df["Salary"]>40000)]
print(mule)