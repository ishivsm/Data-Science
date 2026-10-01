import pandas as pd

df = pd.DataFrame({
    "Age": ["25", "30", "35"],
    "Salary": ["40000", "50000", "60000"]
})

print(df.dtypes)

df["Age"] = df["Age"].astype(int)

print(df.dtypes)

#Marathi: String स्वरूपातील numbers ला integer मध्ये convert केले.