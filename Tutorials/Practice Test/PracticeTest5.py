n = int(input("Enter n value: "))
fac = 1
if n==0:
    print("1")
elif n==1:
    print("1")
else:
    for value in range(1,n+1):
        fac = fac*value
    print(fac)