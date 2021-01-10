print("Python Program for How to check if a given number is Fibonacci number?\n")

n=int(input("Enter the number: "))
c=0
a=1
b=1
if n==0 or n==1:
    print("Yes")
else:
    while c<n:
        c=a+b
        b=a
        a=c
    if c==n:
        print("Yes")
    else:
        print("No")

print("--------------------------------------\n")

def fib(num):
    c = 0
    a = 1
    b = 1
    if num ==0 or num ==1:
        return True
    else:
        while c <num:
            c = a+b
            a = b
            b = c
        if c == num:
            return True
        else:
            return False

print(n,"is a fibenocci number:",fib(n))
