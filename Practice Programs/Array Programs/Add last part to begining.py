print("Python Program to Split the array and add the last part to the begining")

l = [10,20,30,40,50,60]
n = 2
p = len(l)

print("New Array is",l[p-n:]+l[:p-n])

print("----------------------------\n")

def split(arr,n):
    ln = len(arr)
    s1 = arr[ln-n:]
    s2 = arr[:ln-n]
    return s1+s2

k = split(l,n)
print("New Array is:",k)

