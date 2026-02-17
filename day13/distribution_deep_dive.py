import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

data = {
    "Price": np.random.gamma(shape=2, scale=200000, size=200),  # Right-skewed prices
    "City": np.random.choice(["Bangalore", "Mumbai", "Delhi", "Chennai"], size=200)
}

df = pd.DataFrame(data)
print(df.head())

plt.figure(figsize=(8,5))
sns.histplot(df['Price'], kde=True)
plt.title("Distribution of House Prices")
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.show()

print("Skewness:", df['Price'].skew())
print("Kurtosis:", df['Price'].kurt())

plt.figure(figsize=(8,5))
sns.countplot(x='City', data=df)
plt.title("Number of Houses in Each City")
plt.show()

print(df['City'].value_counts())

