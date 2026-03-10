def simple(p,n,r):
    si = p*n*r/100
    tc = si+p
    return si,tc
p = int(input("principle amount is:"))
n = int(input("no of days is:"))
r = int(input("rate of interest is:"))
result = simple(p,n,r)
print("simple interest is:",result)
print("total cost is:",result)
