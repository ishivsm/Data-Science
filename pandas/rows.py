import pandas as pd
df=pd.read_json("numpy_practice_25000.json")
print(df)
print("Display 10 rows")
print(df.head())
print("dispalay 10 rows last")
print(df.tail())