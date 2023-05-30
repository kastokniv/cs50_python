students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        ## creates 2 key and value for and empty string name and house
        student = {"name": name, "house": house}
        students.append(student)


## get name for sorting the output accordingly
# def get_name(student):
# return student["name"]


## assign the value from the get_name to sort according to the name, to reverse use ", reverse=True"
## use lambda function if you use the function only once.
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['house']}")
