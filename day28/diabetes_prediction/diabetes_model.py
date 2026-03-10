# TASK 3 : Predict Diabetes using Decision Tree

# Step 1 — Import libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# Step 2 — Load dataset
df = pd.read_csv("diabetes.csv")

print("First 5 rows:")
print(df.head())


# Step 3 — Define features and target
X = df.drop("Outcome", axis=1)
y = df["Outcome"]


# Step 4 — Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Step 5 — Create Decision Tree Model
model = DecisionTreeClassifier(random_state=42)


# Step 6 — Train Model
model.fit(X_train, y_train)


# Step 7 — Predictions
y_pred = model.predict(X_test)


# Step 8 — Model Evaluation
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# Step 9 — Visualization
sns.countplot(x="Outcome", data=df)
plt.title("Diabetes Distribution")
plt.show()