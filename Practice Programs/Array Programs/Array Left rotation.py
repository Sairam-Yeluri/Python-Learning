print("Python Program for Left array rotation\n")

l = [10,20,30,40,50,60]
v = 2  #Number of elements to shift

def leftrotate(arr,n):

    for i in range(n):
        temp = arr[0]
        l =len(arr)
        for j in range(0,l-1):
            arr[j] =arr[j+1]
        arr[l-1]=temp
    return arr

p = leftrotate(l,v)
print("Left rotate is:\n",p)

print("----------------------------\n")
print("SIMPLE METHOD")

l = [10,20,30,40,50,60]
n = 8
if n >len(l):
    k = n%len(l) #8%6 = 2
else:
    k =n

print(l[k:]+l[:k])