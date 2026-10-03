"""
1- how big is ur dataset
2- what are the names of columns

shape is attribute and columns is attribute


"""

import pandas as pd

df = pd.DataFrame({
    "Name": ["A", "B", "C"],
    "Age": [20, 25, 30],
    "Salary": [20000, 30000, 40000]
})

print(df.shape)
print(df.columns)