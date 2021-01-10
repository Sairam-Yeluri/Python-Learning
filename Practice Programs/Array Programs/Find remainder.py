print("Python Program for Find remainder of array multiplication divided by n")

arr = [10,2,3,4,5,6]
n = 50
val = 1

for i in arr:
    val = val * i
print("Remainder is",val/n)

print("------------------------------\n")

def remainder(l,val):
    result = 1
    for i in l:
        result = result * i
    return result/val

k = remainder(arr,n)
print("Remainder is",k)

