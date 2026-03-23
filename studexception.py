class Students:
    def details(self):
        self.name = input("enter a student name:")
        while True:
            try:
                self.id = int(input("enter a student Roll no:"))
                break
            except ValueError as e:
                print("Invalid input, Enter a number")
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
               if 0<=mark<=100:
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
         with open("stud1.txt", "a") as s:
           s.write("\t\t\t\t STUDENT DETAILS\n\n")
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
stu = Students()
stu.details()
stu.display()
stu.savefile()








