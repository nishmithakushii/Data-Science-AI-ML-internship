import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

np.random.seed(42)

square_footage = np.random.randint(500, 3000, 200)
bedrooms = square_footage // 300  # correlated with size
price = square_footage * 5000 + bedrooms * 100000 + np.random.normal(0, 200000, 200)

data = {
    "SquareFootage": square_footage,
    "Bedrooms": bedrooms,
    "Price": price,
    "City": np.random.choice(["Bangalore", "Mumbai", "Delhi", "Chennai"], 200)
}

df = pd.DataFrame(data)

print(df.head())

correlation_matrix = df.corr(numeric_only=True)
print(correlation_matrix)

plt.figure(figsize=(8,5))
sns.boxplot(y=df['Price'])
plt.title("Boxplot of House Prices")
plt.show()

