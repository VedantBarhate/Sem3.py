

class Student:
    def __init__(self, name, rno, grade):
        self.name = name
        self.rno = rno
        self.grade = grade

    def show_details(self):
        print(f"Name: {self.name}")
        print(f"Roll no: {self.rno}")
        print(f"Grade: {self.grade}")


stu1 = Student("John", 12, "A")
stu1.show_details()
stu2 = Student("Andrew", 22, "B")
stu2.show_details()