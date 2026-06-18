import pandas as pd

# Update this line to handle the special characters
df = pd.read_csv("data/superstore.csv", encoding="ISO-8859-1")

# The rest of your script remains exactly the same
n = len(df)
day_1 = df.iloc[: int(n * 0.8)]
day_2 = df.iloc[int(n * 0.8) : int(n * 0.9)]
day_3 = df.iloc[int(n * 0.9) :]

# Save them as clean, standard UTF-8 files for Databricks
day_1.to_csv("day_1.csv", index=False, encoding="utf-8")
day_2.to_csv("day_2.csv", index=False, encoding="utf-8")
day_3.to_csv("day_3.csv", index=False, encoding="utf-8")

print("Files successfully split into day_1.csv, day_2.csv, and day_3.csv!")