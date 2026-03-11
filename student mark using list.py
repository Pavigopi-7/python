student=[]
mark1 = int(input("enter a tamil mark:"))
mark2 = int(input("enter a english mark:"))
mark3 = int(input("enter a math marks:"))
tot = mark1+mark2+mark3
print("TOTAL MARKS IS:",tot)
avg = tot/3
print("AVERAGE IS:",avg)
if avg>=100 and avg<=90:
    print("grade A+")
elif avg>=90 and avg<=80:
    print("grade A")
elif avg>=80 and avg<=70:
    print("grade B+")
elif avg>=70 and avg<=60:
    print("grade B")
elif avg>=60 and avg<=50:
    print("grade C")
else:
    print("your fail")
student.append(mark1)
print(student)
student.append(mark2)
print(student)
student.append(mark3)
print(student)