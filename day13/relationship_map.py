import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

# Create square footage
square_footage = np.random.randint(500, 3000, 200)

# Price correlated with square footage
price = square_footage * 5000 + np.random.normal(0, 200000, 200)

data = {
    "SquareFootage": square_footage,
    "Price": price,
    "City": np.random.choice(["Bangalore", "Mumbai", "Delhi", "Chennai"], 200)
}

df = pd.DataFrame(data)

print(df.head())

plt.figure(figsize=(8,5))
sns.scatterplot(x='SquareFootage', y='Price', data=df)
plt.title("Square Footage vs Price")
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(x='City', y='Price', data=df)
plt.title("Price Distribution Across Cities")
plt.show()
