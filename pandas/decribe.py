import pandas as pd

df = pd.DataFrame({
    "Age": [20, 25, 30, 35, 40],
    "Salary": [20000, 30000, 40000, 50000, 60000]
})

print(df.describe())