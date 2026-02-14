import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5]
sales = [100, 150, 200, 180, 220]

plt.plot(months, sales, label="Sales")

plt.title("Monthly Sales Report",fontsize=12)
plt.xlabel("Month",color="blue")
plt.ylabel("Sales Amount")
plt.legend() 
plt.grid(True)

plt.show()