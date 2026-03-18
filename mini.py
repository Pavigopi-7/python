contacts={}
def add():
    name = input("contact name:")
    phoneno = input("phoneno:")
    mailid = input("Mailid")
    contacts[name]={"phoneno":phoneno,"Mailid":mailid}
    print("contacts are added successfully")

def search():
    searchname = input("enter a name to be search:")
    if searchname in contacts:
        print("Name:",searchname)
        print("phoneno:",contacts[searchname]["phoneno"])
        print("Mailid:",contacts[searchname]["Mailid"])
    else:
        print("contacts not found in the dictionary")

def view():
    if not contacts:
        print("contacts list is empty in the dictionary")
    else:
        print("Name\t\tphoneno\t\t\tMailid")
        for name, details in contacts.items():
            print(f"{name}\t\t{details['phoneno']}\t\t\t{details['Mailid']}")

def update():
    editcontact = input("enter a contact to be edited:")
    if editcontact in contacts:
        phoneno = input("enter a new phoneno:")
        mailid = input("enter a mailid that u have to be save:")
        contacts[editcontact]={"Phoneno":phoneno, "Mailid":mailid}
        print("Edited contact updated successsfully")
    else:
        print("Given contacts does not exists in the dictionary")
view()

def delete():
    deletecontact = input("enter a contact name to be deleted:")
    if deletecontact in contacts:
        confirm = input("Are u sure u want to delete the contact: (yes/no)")
        if confirm.lower()=='yes':
            contacts.pop(deletecontact)
        else:
            print("Deletion cancelled")
    else:
        print("contact not found in the dictionary")

while True:
    print("CONTACTS BOOK APPLICATION:")
    print("1. Add a new contact:")
    print("2. View a contact list in the dictionary:")
    print("3. Search a contact from a dictionary:")
    print("4. Update a contact to the dictionary:")
    print("5. Delete a contact from the dictionary:")
    print("6. Exit:")
    ch = int(input("enter a operation to be performed:"))
    if ch==1:
       add()
    elif ch==2:
       view()
    elif ch==3:
       search()
    elif ch==4:
        update()
    elif ch==5:
        delete()
    elif ch==6:
       print("Exiting the program")

