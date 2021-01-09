n=int(input("Enter n value: "))
print()
for i in range(n):
    for j in range(n):
        print(" * ",end="")
    print()
print()
for i in range(n):
    for j in range(i+1):
        print(" * ",end="")
    print()
print()
for i in range(n):
    for j in range(n):
        if i>j:
           print("   ",end="")
        else:
            print(" * ",end="")
    print()
print()
for i in range(n):
    for j in range(n-i):
        print(" * ",end="")
    print()
print()
for i in range(n):
    for j in range(n,i,-1):
        print("   ",end="")
    for k in range(i+1):
        print(" * ",end="")        
    print()

print("\n--------------------------\n")

p = 1
for i in range(n,0,-1):
    for j in range(i,0,-1):
        print("  ",end="")
    print(" *"*p)
    p = p+2

print()

d = (2*n)-1
for i in range(n,0,-1):
    for j in range(i,n):
        print("  ",end="")
    print(" *"*d)
    d = d-2
