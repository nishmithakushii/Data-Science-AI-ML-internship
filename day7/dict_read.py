import csv

with open("student.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["name"], row["grade"], row["status"])
        
with open("student.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)