print("\nPython Program to check Armstrong Number\n")

num = int(input("Enter number: "))
temp = num
sum = 0

while temp>0:
    digit = temp%10
    sum = sum + digit**3
    temp = temp//10

if sum == num:
    print(num,"is an Armstrong number")
else:
    print(num,"is Not an Armstrong number")

print("-------------------------------------------\n")

def armstrong(n):
    temp = num
    s = 0
    while temp>0:
        digit = temp%10
        s = s + digit**3
        temp = temp//10
    if sum == num:
        return True
    else:
        return False


print(num,"is an Armstrong number: ",armstrong(num),"\n")
