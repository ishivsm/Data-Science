import pandas as pd
employees = pd.DataFrame({
    "Employee_ID": [101, 102, 103],
    "Name": ["Amit", "Priya", "Rahul"],
    "Dept_ID": [1, 2, 1]
})

departments = pd.DataFrame({
    "Department_ID": [1, 2, 3],
    "Department": ["IT", "HR", "Sales"]
})

result = pd.merge(
    employees,
    departments,
    left_on="Dept_ID",
    right_on="Department_ID",
    how="inner"
)

print(result)

"""
cross join 
1df=m rows
2df= mrows

m*n
"""