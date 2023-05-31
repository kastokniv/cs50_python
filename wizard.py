class Wizard:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name


## calling Wizard superclass in Student class
class Student(Wizard):
    def __init__(self, name, house):
        ##inheriting the name from the super class of Wizard
        super().__init__(name)
        self.house = house

    ...


## calling Wizard superclass in Student class
class Professor(Wizard):
    def __init__(self, name, subject):
        ##inheriting the name from the super class of Wizard
        super().__init__(name)
        self.subject = subject

    ...


wizard = Wizard("Albus Dumbeldore")
student = Student("Harry", "Gryffindor")
professor = Professor("Severus", "Defense Against the Dark Arts")
