#Factorial of number

def factorial(val):
    if ((val == 0) or (val ==1)):
        return 1
    else:
        return val * factorial(val - 1)


r1 = factorial(5)
print(r1)

r2 = factorial(0)
print(r2)

r3 = factorial(1)
print(r3)