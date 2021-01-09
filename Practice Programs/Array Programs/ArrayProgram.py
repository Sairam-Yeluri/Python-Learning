from array import *

arr = array("i",[]) #Initialize an empty array

n = int(input("Enter Array Length: "))

for i in range(n):
    x = int(input("Enter the value: "))
    arr.append(x)

print("Your array is: ",arr)

a =input("Do you want to find a value? (y/n): ")
if a=="Y" or a =="y":
    s = 0
    v = int(input("Enter which value: "))
    for p in arr:
        if p == v:
            print (v,"is Found and the position is:",s+1)
        else:
            s+=1

