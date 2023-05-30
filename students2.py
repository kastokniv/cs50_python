import csv

students = []

with open("students2.csv") as file:
    ## it's a function of csv module
    # reader = csv.reader(file)
    # for name, home in reader:
    reader = csv.DictReader(file)
    for row in reader:
        ## define name, home at the top of the csv file
        students.append({"name": row["name"], "home": row["home"]})

## use lambda function if you use the function only once.
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is from {student['home']}")
