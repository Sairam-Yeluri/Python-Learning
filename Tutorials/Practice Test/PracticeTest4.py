n = int(input("Enter n value: "))
sum = 0
for value in range(n+1):
    sum = sum + value
print("Sum of n numbers is",sum)
print("Average of n numbers is: ",sum/n)