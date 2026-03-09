a = int(input("enter a number:"))
b = int(input("enter a number:"))
ch = 0
while ch<5:
    print ("calculator menu:")
    print("1.add 2,sub,3.mul,4.div 5.exit")
    ch = int (input("enter your choice:"))
    if ch == 1:
        c =a+b
        print("add is :",c)
    elif ch == 2:
        c =a-b
        print("sub is :",c)
    elif ch == 3:
        c = a*b
        print("mul is :",c)
    elif ch == 4:
        c = a/b
        print("div is :",c)
    elif ch == 5:
        break
    else:
        print("invalid")
