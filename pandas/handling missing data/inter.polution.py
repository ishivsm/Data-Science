import pandas as pd
import numpy as np

df = pd.DataFrame({
    "Sales": [100, 200, np.nan, 400, 500]
})
df["Sales"] = df["Sales"].interpolate()


#df["column"].interpolate()

#df["Sales"].interpolate(method="linear")
print(df)