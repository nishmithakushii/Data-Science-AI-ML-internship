# TASK 1 : Predict Student Pass or Fail using Decision Tree

# Step 1 — Import Libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


# Step 2 — Load Dataset
df = pd.read_csv("StudentsPerformance.csv")

print("First 5 rows of dataset:")
print(df.head())


# Step 3 — Create Average Score
df["average_score"] = (df["math score"] +
                       df["reading score"] +
                       df["writing score"]) / 3


# Step 4 — Create Pass / Fail column
# If average score >= 40 → Pass (1)
# If average score < 40 → Fail (0)

df["pass"] = df["average_score"].apply(lambda x: 1 if x >= 40 else 0)

print("\nDataset after adding pass column:")
print(df.head())


# Step 5 — Convert categorical columns to numbers
df = pd.get_dummies(df, drop_first=True)


# Step 6 — Define Features and Target
X = df.drop("pass", axis=1)
y = df["pass"]


# Step 7 — Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)


# Step 8 — Create Decision Tree Model
model = DecisionTreeClassifier(random_state=42)


# Step 9 — Train the Model
model.fit(X_train, y_train)


# Step 10 — Make Predictions
y_pred = model.predict(X_test)


# Step 11 — Model Evaluation
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))


# Step 12 — Visualization
sns.countplot(x="pass", data=df)
plt.title("Pass vs Fail Distribution")
plt.show()