class Student:
   def __init__(self):
       self.name = input("Enter a Student name:")
       self.id =int(input("Enter a Student Roll number:"))
       self.age = int(input("Enter a Student Age:"))
       self.m1 = self.getmarks("Tamil:")
       self.m2 = self.getmarks("English:")
       self.m3 = self.getmarks("Maths:")
       self.m4 = self.getmarks("Science:")
       self.m5 = self.getmarks("Social Studies:")

       self.tot = self.m1 + self.m2 + self.m3 + self.m4 + self.m5
       self.avg = self.tot / 5
   def getmarks(self, subject):
      while True:
         try:
            mark = int(input(f"Enter your {subject} marks"))
            if 0 <= mark <= 100:
                return mark
            else:
                print("Marks should be between 0 and 100")
         except ValueError:
            print("Invalid input. sry give valid input")
   def display(self):
      print("Student name:", self.name)
      print("Roll Number:", self.id)
      print(self.name, "Marks obtained:")
      print("Tamil:", self.m1)
      print("English:", self.m2)
      print("Maths:", self.m3)
      print("Science:", self.m4)
      print("Social studies:", self.m5)
      print("Your Total marks out off 500 is:", self.tot)
      print("your Average is:", self.avg)


   def savefile(self):
      with open("stud2.txt","a") as s:
        s.write("\t\t\t\t    STUDENT DETAILS \n\n")
        s.write(f"\nName:{self.name}\n")
        s.write(f"Roll number: {self.id}\n")
        s.write(f"Tamil: {self.m1}\n")
        s.write(f"English: {self.m2}\n")
        s.write(f"Maths: {self.m3}\n")
        s.write(f"Science: {self.m4}\n")
        s.write(f"Social studies: {self.m5}\n")
        s.write(f"Total marks: {self.tot}\n")
        s.write(f"Average is: {self.avg}\n")
        s.write("-" * 30 + "\n")

class System(Student):
    def __init__(self):
        self.students = {}

    def add(self, Student):
        if Student.id in self.students:
            print("Already Exist in the record")
        else:
            self.students[Student.id]=Student
            Student.savefile()
            print("Student record added successfully")

    def view(self):
        if not self.students:
            print("No such records found")
        else:
            for sid,Student in self.students.items():
                Student.display()

    def update(self, sid, name=None,age=None):
        if sid in self.students:
            if name:
                self.students[sid].name=name
            if age:
                self.students[sid].age=age
            print("Student updated successfully")
        else:
            print("Student record not found")

    def delete(self, sid):
        if sid in self.students:
            del self.students[sid]
            print("deleted successfully")
        else:
            print("Student record not found")

sys = System()

stud = Student()
stud.savefile()
sys.add(stud)
sys.view()
sid = int(input("Enter your id to update:"))
sys.update(sid,name="updated name")
sid = int(input("Enter your id:"))
sys.delete(sid)
