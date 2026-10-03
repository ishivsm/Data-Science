import pandas as pd
df = pd.DataFrame({
    "Salary": ["40000", "50000", "ABC", "60000"]
})

df["Salary"]=pd.to_numeric(
    df["Salary"],
    errors="coerce"
)
print(df)