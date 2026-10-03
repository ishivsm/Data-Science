import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Name": ["Rahul", "Amit", "Priya", "Sneha"],
    "Age": [22, np.nan, 24, 28],
    "Salary": [30000, 45000, np.nan, 60000]
})

print(df)

print(df.isnull())

print(df.isnull().sum())