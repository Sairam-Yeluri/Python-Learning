num = int(input("Enter a number: "))

for n in range(2,num):
    if num%n==0:
        print(num,"is Not a Prime")
        break

else:
    print(num,"is a Prime")

print("------------------------------\n")

def prime(num):
    for n in range(2,num):
        if num%n==0:
            print(num,"is Not a Prime")
            break

    else:
        print(num,"is Prime")

prime(num)
