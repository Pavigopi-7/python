class Saving:
    def details(self):
        self.fullname = input("Enter your Fullname:")
        self.dob = input("Enter your dob:")
        self.sex = input("enter your gender:")
        self.occupation = input("enter your occupation:")
        self.address = input("enter your address:")

    def display1(self):
        print("Fullname:",self.fullname)
        print("Date of birth:",self.dob)
        print("Gender:",self.sex)
        print("Occupation:",self.occupation)
        print("Address:",self.address)

class Proof(Saving):
    def proofdetails(self):
        self.aadhaar = input("Enter your Aadhaar card no:")
        self.passport = input("enter your Passport no:")
        self.voter = input("enter your voterid no:")
        self.driving = input("enter your driving license no:")

    def display2(self):
        print("Aadhar card no:",self.aadhaar)
        print("Passport no:",self.passport)
        print("Voterid no:",self.voter)
        print("Driving license no:",self.driving)
save = Saving()
save.details()
save.display1()
pf = Proof()
pf.proofdetails()
pf.display2()
