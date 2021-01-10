print("Python Program for n-th Fibonacci number\n")

print("N Fibonacci numbers:")
n = int(input("Enter number: "))
a = 0
b = 1
if  n < 0:
    print("Invalid Number")
elif n==0:
    print(a)
elif n ==1:
    print(b)

else:
    print(a)
    print(b)
    for val in range(2,n):
        c = a+b
        a = b
        b = c
        print(c)

print("----------------------------\n")
def fib(num):

    if num<0:
        return "Invalid Number"
    elif num==1:
        return 0
    elif num ==2:
        return 1
    else:
        return fib(num-1)+fib(num-2)

r = fib(n)
print(n,"th fibanoci number is",r)
    

