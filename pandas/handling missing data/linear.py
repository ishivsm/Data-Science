import pandas as pd

dagta={
    'Time':[1,2,3,4,5],
    'Value':[10,None,30,None,50]
}

df=pd.DataFrame(dagta)
print('b efore')

print(df)

df['Value']=df['Value'].interpolate(method="linear")
print("after")
print(df)

"""
1-timer series data
2-numeric data following trend
3-avoid droping rows
#not use in categorical


"""