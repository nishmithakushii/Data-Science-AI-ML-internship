import csv

data=[
     ["Name", "Score"],
    ["John", 85],
    ["Emily", 55]
]

with open("result.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(data)
