## By using classes
class Student:
    ## __init__ is called as the constructor
    def __init__(self, name, house):
        ## self.name is instance variable which is beign created in get_student student = Student(name, house)

        ## if user does not input any name and enter
        # if not name:
        # raise ValueError("Missing Name")
        # if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
        # raise ValueError("Invalid House")

        self.name = name
        self.house = house
        # self.patronus = patronus

    def __str__(self):
        return f"{self.name} is from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing Name")
        self._name = name

    ## getter # @property is called as getter in python
    @property
    def house(self):
        return self._house

    ## setter # .setter is called as setter in python
    ## variable and function in same class cannot have same name so self._house is used to call from __init__
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid House")
        self._house = house

    ## any method in a class takes atleast one arugement and returns
    # def charm(self):
    # match self.patronus:
    # case "Stag":
    # return "🦄"
    # case "Otter":
    # return "🦔"
    # case "Jack Russel Terrier":
    # return "🐹"
    # case _:
    # return "/"


def main():
    student = get_student()
    # student._house = "Number Four, Pivet Drive"
    print(student)

    # if student["name"] == "Padma":
    # student["house"] = "Ravenclaw"
    # print(f"{student.name} from {student.house}")

    # print("Expecto Patronum!")
    # print(student.charm())


def get_student():
    name = input("Name: ")
    house = input("House: ")
    # patronus = input("Patronus: ")
    return Student(name, house)


if __name__ == "__main__":
    main()
