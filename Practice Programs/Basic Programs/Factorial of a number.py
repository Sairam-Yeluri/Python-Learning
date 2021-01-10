print("Python Program for factorial of a number")

def factorial(n):
    result = n
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        result = result * factorial(n-1)
        return result

k = factorial(-5)
print("factorial is",k)