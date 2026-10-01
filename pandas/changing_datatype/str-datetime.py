import pandas as pd
df = pd.DataFrame({
    "Date": ["2026-01-10", "2026-02-15", "2026-03-20"]
})


df["Year"] = df["Date"].dt.year
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day
df["Day_Name"] = df["Date"].dt.day_name()
df["Month_Name"] = df["Date"].dt.month_name()
print(df.dtypes)
df["Date"] = pd.to_datetime(df["Date"])
print(df)
print(df.dtypes)

"""
| Method               | Use                                 |
| -------------------- | ----------------------------------- |
| `astype(int)`        | Convert to integer                  |
| `astype(float)`      | Convert to float                    |
| `astype(str)`        | Convert to string                   |
| `astype(bool)`       | Convert to boolean                  |
| `astype("category")` | Convert to category                 |
| `pd.to_numeric()`    | Convert to numeric                  |
| `pd.to_datetime()`   | Convert to date/time                |
| `pd.to_timedelta()`  | Convert to time duration            |
| `convert_dtypes()`   | Automatically choose suitable types |


"""
#Most important for Data Science
df.dtypes
df["Age"] = df["Age"].astype(int)
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
df["Date"] = pd.to_datetime(df["Date"])
df = df.convert_dtypes()
