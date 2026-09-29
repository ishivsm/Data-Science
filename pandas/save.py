import pandas as pd
data={
    "name":["ram","ajay"],
    "age":[25,30],
    "city":["pune","nagpur"]

}


df=pd.DataFrame(data)
print(df)

#df.to_csv("putput.csv",index=False) 
#df.to_excel("putput.xlsx",index=False) 
df.to_json("putput.json",index=False) 