l = [10,20,30,40,50,60]
n = 2 

print("New Array is:",l[n:]+l[:n])

print("----------------------------\n")

def split(arr,n):
    s1 = arr[:n]
    s2 = arr[n:]
    return s2+s1

k = split(l,n)
print("New Array is:",k)