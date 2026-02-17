import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

data={
    "Age": [25,30,35,40,28,32,45,50,23,36,29,41],
    "Salary": [30000,40000,50000,65000,42000,48000,80000,90000,28000,52000,46000,70000],
    "Experience": [2,5,10,15,3,7,20,25,1,8,6,12],
    "Department": ["HR", "IT", "Finance", "IT", "HR", "Finance", "IT", "HR", "Finance", "IT", "HR", "Finance"],
    "Gender": ["Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female", "Male", "Female"]
}
df = pd.DataFrame(data)
print(df)

plt.figure()
sns.scatterplot(x="Age", y="Salary", data=df)
plt.title("Age vs Salary")
plt.show()

plt.figure()
sns.scatterplot(x="Experience", y="Salary", data=df)
plt.title("Experience vs Salary")
plt.show()

plt.figure()
sns.boxplot(x="Gender", y="Salary", data=df)
plt.title("salary by Gender")
plt.show()

plt.figure()
sns.boxplot(x="Department", y="Salary", data=df)
plt.title("salary by Department")
plt.show()

corr_matrix = df.corr(numeric_only=True)
print("\nCorrelation Matrix:")
print(corr_matrix)

plt.figure()
sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()  

plt.figure()
sns.boxplot(x=df["Age"])
plt.title("Age outliers")
plt.show()

plt.figure()
sns.boxplot(x=df["Experience"])
plt.title("Experience outliers")
plt.show()

#FINAL STEP — DOCUMENT INSIGHTS (PRINT SAMPLE INSIGHTS)
# Students should write their own observations here.


print("\n===== SAMPLE INSIGHTS =====")
print("1. Salary increases with Experience and Age (positive correlation).")
print("2. Finance department shows higher salary range.")
print("3. No extreme outliers detected in Age or Experience.")
print("4. Gender distribution appears balanced.")
print("5. Experience strongly influences Salary.")