# TASK 2 : Predict Car Price using Decision Tree Regressor

# Step 1 — Import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, r2_score


# Step 2 — Load dataset
df = pd.read_csv("car data.csv")

print("First 5 rows of dataset:")
print(df.head())


# Step 3 — Check dataset info
print("\nDataset Info:")
print(df.info())


# Step 4 — Convert categorical columns to numbers
df = pd.get_dummies(df, drop_first=True)


# Step 5 — Define features and target
X = df.drop("Selling_Price", axis=1)
y = df["Selling_Price"]


# Step 6 — Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Step 7 — Create Decision Tree Regressor
model = DecisionTreeRegressor(random_state=42)


# Step 8 — Train model
model.fit(X_train, y_train)


# Step 9 — Make predictions
y_pred = model.predict(X_test)


# Step 10 — Evaluate model
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\nMean Absolute Error:", mae)
print("R2 Score:", r2)


# Step 11 — Visualization
sns.scatterplot(x=y_test, y=y_pred)
plt.xlabel("Actual Price")
plt.ylabel("Predicted Price")
plt.title("Actual vs Predicted Car Price")
plt.show()