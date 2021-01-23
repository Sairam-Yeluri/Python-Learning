num1 = int(input("Enter starting number: "))
num2 = int(input("Enter ending number: "))

for n in range(num1, num2):
    if n > 1:
        for k in range(2,n):
            if n%k==0:
                break
        else:
            print(n)
print("----------------------\n")

def prime(num1,num2):
    l = []
    for n in range(num1, num2):
        if n > 1:
            for k in range(2,n):
                if n%k==0:
                    break
            else:
                l.append(n)
    return l

k = prime(num1,num2)
print("Prime numbers are",k)



    

