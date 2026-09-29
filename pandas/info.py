
#info summariyy of a data frane
import pandas as pd
df=pd.read_csv("numpy_practice_25000.csv")
df.info()
print(df.describe())
print(df.shape)
print(df.columns)