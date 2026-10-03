import pandas as pd

data={
    "Employee": [
        "Amit", "Priya", "Rahul", "Sneha", "Vijay",
        "Neha", "Akash", "Pooja", "Rohit", "Anjali"
    ],

    "Department": [
        "IT", "HR", "IT", "Sales", "HR",
        "IT", "Sales", "Finance", "IT", "Finance"
    ],

    "City": [
        "Pune", "Mumbai", "Pune", "Delhi", "Mumbai",
        "Pune", "Delhi", "Mumbai", "Delhi", "Pune"
    ],

    "Age": [25, 32, 28, 24, 35, 29, 26, 31, 27, 30],

    "Salary": [
        45000, 65000, 55000, 35000, 70000,
        60000, 40000, 75000, 50000, 68000
    ],

    "Experience": [2, 7, 4, 1, 9, 5, 3, 8, 4, 6]
}

df=pd.DataFrame(data)

grouped=df.groupby(["City","Department"])["Salary"].sum()
print(grouped)