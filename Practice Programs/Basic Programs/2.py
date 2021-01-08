
print("Maximum of two numbers in Python")

num1 = int(input("Enter first number:"))
num2 = int(input("Enter first number:"))
print("Max value is",max(num1,num2))

print("method2")

def max_val(num1,num2):
    if num1> num2:
        return num1
    elif num1< num2:
        return num2
    else:
        return "Both are Equal and value is",num1

r = max_val(num1,num2)
print("Max value is",r)
        