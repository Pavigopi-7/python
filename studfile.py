class Student:
    def details(self):
        self.name = input("enter your name:")
        self.id = int(input("enter your Roll number:"))
        self.m1 = int(input("enter your Tamil mark:"))
        self.m2 = int(input("enter your English mark:"))
        self.m3 = int(input("enter your Maths mark:"))
        self.m4 = int(input("enter your Science mark:"))
        self.m5 = int (input("enter your Socialstudies mark:"))
        self.tot = self.m1+self.m2+self.m3+self.m4+self.m5
        self.avg = self.tot/5
    def display(self):
        print("Student name:", self.name)
        print("Roll Number:", self.id)
        print(self.name,"Marks obtained:")
        print("Tamil:", self.m1)
        print("English:", self.m2)
        print("Maths:", self.m3)
        print("Science:", self.m4)
        print("Socialstudies:", self.m5)
        print("Your Total marks outoff 500 is:",self.tot)
        print("your Average is:",self.avg)

    def savefile(self):
        with open("stud.txt","a") as s:
         s.write("\t\t\t\t STUDENT DETAILS\n\n")
         s.write(f"\nName:{self.name}\n")
         s.write(f"Roll number: {self.id}\n")
         s.write(f"Tamil: {self.m1}\n")
         s.write(f"English: {self.m2}\n")
         s.write(f"Maths: {self.m3}\n")
         s.write(f"Science: {self.m4}\n")
         s.write(f"Socialstudies: {self.m5}\n")
         s.write(f"Total marks: {self.tot}\n")
         s.write(f"Average is: {self.avg}\n")
         s.write("-" * 30 + "\n")
stu = Student()
stu.details()
stu.display()
stu.savefile()

