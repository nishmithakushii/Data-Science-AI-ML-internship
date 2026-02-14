import pandas as pd

data = {
    "location": [" New York", "new york", "NEW YORK ", "Los Angeles", "los angeles "]
}

df = pd.DataFrame(data)

print("Before cleaning:")
print(df["location"].unique())

df["location"] = df["location"].str.strip()
df["location"] = df["location"].str.lower()

print("\nAfter cleaning:")
print(df["location"].unique())
