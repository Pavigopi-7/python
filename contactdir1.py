contact={}
n = int(input("enter a no.of details:"))
for x in range(n):
    name = input("enter a name:")
    mobileno = input("enter a mobileno:")
    if name=="john":
        print("john is the 45th person in the list")
    else:
        print("sorry try again")
contact[name]=mobileno
print(contact)
print(contact.keys())
print(contact.values())
contact.pop(name)
print(contact)
contact["color"]="red"
print(contact)

