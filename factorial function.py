def factorial(n):
    fact = 1
    if n==0:
        return 1
    else:
        for i in range(1,n+1):
            fact = fact*i
            return fact
        n = int(input("enter a no:"))
        result = factorial(n)
        print("factorial is:",result)


