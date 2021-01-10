
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def add_sub(x,y):
    a = x+y
    s = x-y
    return a,s

result1,result2 = add_sub(num1,num2)

print("Addition is:",result1)
print("Substraction is:",result2)