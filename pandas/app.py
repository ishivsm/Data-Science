import pandas as pd
#read data from csv file into a data frame
df=pd.read_csv("numpy_practice_25000.csv")
print(df)

df=pd.read_json("numpy_practice_25000.json")
print(df)
"""df=pd.read_excel("numpy_practice_25000.xlxs")
print(df)"""