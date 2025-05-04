class Student:

    Uni = "KBTU"

    def __init__(self, name = "Unknown", group = "Unknown", studID = 0, gpa = 1.0):
        self.name = name
        self.group = group
        self.studentID = studID
        self.gpa = gpa

    def __bool__(self):
        return self.gpa >= 2.0

    def __str__(self):
        return f"Student {self.name} have gpa {self.gpa}"

    def sayHello(self):
        print(f"Hello, my name is {self.name}. I study in {self.group} group")

    def Info(self):
        print("Name: ", self.name)
        print("Group: ", self.group)
        print("ID: ", self.studentID)
        print("University", self.Uni)

s1 = Student("Mansur", "GE84932", 12, 2.5)

print(bool(s1))
print(s1)

