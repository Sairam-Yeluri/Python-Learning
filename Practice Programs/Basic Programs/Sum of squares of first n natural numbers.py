num = int(input("Enter number: "))
sum = 0

while num > 0:
    sum = sum+(num*num)
    num = num-1

print("Sum of squares of first n natural numbers is:",sum)

print("------------------------------")

def squares(n):
    sm = 0
    for i in range(1, n+1) : 
        sm = sm + (i * i) 
      
    return sm

print("Sum of squares of first n natural numbers is:",squares(num))

print("\nHere n value is 0 because of while loop so it returns 0")

