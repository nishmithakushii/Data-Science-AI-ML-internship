import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Create dataset

data = {
"Customer_ID": [1001,1002,1003,1004,1005,1006,1007,1008,1009,1010],
"Gender": ["Male","Female","Female","Male","Male","Female","Male","Female","Male","Female"],
"Age": [25,32,28,45,36,23,40,29,31,27],
"City_Tier": [1,2,1,3,2,1,3,2,1,2],
"Avg_Session_Time": [15,10,18,8,12,20,7,16,14,19],
"Pages_Visited": [5,3,6,2,4,8,2,5,6,7],
"Products_Viewed": [3,2,4,1,2,5,1,3,4,4],
"Previous_Purchases": [2,1,3,0,1,4,0,2,3,3],
"Discount_Used": [1,0,1,0,1,1,0,1,1,1],
"Total_Spend": [1200,600,1800,300,900,2500,250,1500,2000,1700]
}

df = pd.DataFrame(data)

#TASK 1: Univariate Analysis

plt.figure()
plt.hist(df["Total_Spend"], bins=5)
plt.title("Distribution of Total Spend")
plt.show()

plt.figure()
plt.boxplot(df["Avg_Session_Time"])
plt.title("Avg Session Time")
plt.show()

plt.figure()
df["City_Tier"].value_counts().plot(kind="bar")
plt.title("City Tier Distribution")
plt.show()

#TASK 2: Bivariate Analysis

plt.figure()
plt.scatter(df["Avg_Session_Time"], df["Total_Spend"])
plt.title("Session Time vs Spend")
plt.show()

plt.figure()
plt.scatter(df["Pages_Visited"], df["Total_Spend"])
plt.title("Pages Visited vs Spend")
plt.show()

plt.figure()
plt.scatter(df["Previous_Purchases"], df["Total_Spend"])
plt.title("Previous Purchases vs Spend")
plt.show()

plt.figure()
sns.boxplot(x="Discount_Used", y="Total_Spend", data=df)
plt.title("Discount vs Spend")
plt.show()

#TASK 3: Multivariate Analysis

plt.figure(figsize=(8,6))
sns.heatmap(df.corr(numeric_only=True), annot=True)
plt.title("Correlation Heatmap")
plt.show()

#TASK 4: Customer Segmentation

fig, axes = plt.subplots(2,2, figsize=(12,10))

axes[0,0].scatter(df["Avg_Session_Time"], df["Total_Spend"])
axes[0,0].set_title("Session vs Spend")

axes[0,1].scatter(df["Previous_Purchases"], df["Total_Spend"])
axes[0,1].set_title("Purchases vs Spend")

sns.boxplot(x="Discount_Used", y="Total_Spend", data=df, ax=axes[1,0])
axes[1,0].set_title("Discount vs Spend")

axes[1,1].hist(df["Total_Spend"])
axes[1,1].set_title("Total Spend Distribution")

plt.tight_layout()
plt.show()
