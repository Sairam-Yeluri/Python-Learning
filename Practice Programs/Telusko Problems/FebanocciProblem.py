num = int(input("Enter Number: "))

def feb(n):
    a = 0
    b = 1
    if n <=0:
        return "Invalid Input"
    elif n==1:
        return a
    elif n == 2:
        return b
    else:
        return feb(n-1) + feb(n-2)

k = feb(num)
print (k)

print("----------------------------")

def feb2(n):
    a = 0
    b = 1
    if n == 0:
        print (a)
    elif n==1 or n ==2:
        print (b)
    else:
        print (a,end=" ")
        print (b,end=" ")
        for i in range(2,n):
            c = a+b
            a = b
            b = c
            print (c,end=" ")

            
feb2(num)

print("\n------------------------------")

def fibo(n,p):
    a = 0
    b = 1
    if n < 0:
        print("invalid value enter a valid one!")
    elif n == 1:
        print(a)
    else:
        print(a,end=" ")
        print(b,end=" ")
        for i in range(2, n):  # 2 elements are printed so 0 and 1 are already occupied now from index 2 start
            c = a+b
            a = b
            b = c
            if c > p:
                break
            print(c,end=" ")


fibo(num,num/2)

