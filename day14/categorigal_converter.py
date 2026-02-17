import pandas as pd

# Create dataset
data = {
    "Transmission": ["Automatic", "Manual", "Manual", "Automatic", "Manual"],
    "Color": ["Red", "Blue", "Green", "Red", "Blue"]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

df["Transmission"] = df["Transmission"].map({
    "Automatic": 0,
    "Manual": 1
})

print("\nAfter Label Encoding:")
print(df)

df = pd.get_dummies(df, columns=["Color"], drop_first=True)

print("\nAfter One-Hot Encoding:")
print(df)

