import pandas as pd

employees = pd.DataFrame({
    "Employee_ID": [101, 102, 103, 104, 105],
    "Name": ["Amit", "Priya", "Rahul", "Sneha", "Vijay"],
    "Department_ID": [1, 2, 1, 3, 2]
})

print(employees)



departments = pd.DataFrame({
    "Department_ID": [1, 2, 3, 4],
    "Department": ["IT", "HR", "Sales", "Finance"],
    "Manager": ["Raj", "Neha", "Kiran", "Pooja"]
})

print(departments)

#commonn column is department id


#1-- inner merge
df_merged=pd.merge(employees,departments,on="Department_ID",how="inner")
print("inner join")
print(df_merged)

print("lEft join")
result = pd.merge(
    employees,
    departments,
    on="Department_ID",
    how="left"
)

print(result)

print("right join")
result = pd.merge(
    employees,
    departments,
    on="Department_ID",
    how="right"

)

print(result)

#outer

result = pd.merge(
    employees,
    departments,
    on="Department_ID",
    how="outer"
)

print(result)

"""
| `how`   | Result                    |
| ------- | ------------------------- |
| `inner` | Matching rows from both   |
| `left`  | All left + matching right |
| `right` | All right + matching left |
| `outer` | All rows from both        |


"""