import pandas as pd

df = pd.read_csv("customer_orders.csv")

print("Data types before conversion:\n")
print(df.dtypes)

df["order_amount"] = df["order_amount"].astype(float)

df["order_date"] = pd.to_datetime(df["order_date"])

print("\nData types after conversion:\n")
print(df.dtypes)
