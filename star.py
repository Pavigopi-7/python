n = int(input("enter a no.of rows:"))
print("no.of rows is:",n)
for i in range(n):
    for j in range(i+1):
        print("*", end=" ")
        print()