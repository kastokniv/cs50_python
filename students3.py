import csv

name = input("What's your name? ")
home = input("Where's your home? ")

## to write the csv file for name and home
with open("students3.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
