class Student:
    def details(self):
        self.name = input("enter your name:")
        self.id = int(input("enter your id number:"))
        self.mark = int(input("enter your marks obtained:"))
    def display(self):
        print("Name:", self.name)
        print("ID number:", self.id)
        print("Marks obtained:", self.mark)
stu = Student()
stu.details()
stu.display()