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
    for j in range(n):
        if i==n-1 or j ==n-1:
            print(" * ",end="")
        else:
            print("   ",end="")
    print()
print()

print("\n--------------------------\n")

k = 2*n - 2
  
for i in range(0, n): 
      
    # inner loop to handle number spaces 
    # values changing acc. to requirement 
    for j in range(0, k): 
        print(end=" ") 
      
    # decrementing k after each loop 
    k = k - 1
      
    # inner loop to handle number of columns 
    # values changing acc. to outer loop 
    for j in range(0, i+1): 
          
        # printing stars 
        print("* ", end="") 
      
    # ending line after each row 
    print("\r") 