print("Python Program for Right array rotation\n")

l = [10,20,30,40,50,60]
v = 2  #Number of elements to shift

def rightrotate(arr,n):

    for i in range(n):
        l =len(arr)
        temp = arr[l-1]
        for j in range(1,l):
            arr[len-j] =arr[len-j-1]
        arr[0]=temp
    return arr

p = rightrotate(l,v)
print("Right shifted array is\n",p)

print("----------------------------\n")
print("SIMPLE METHOD")

l = [10,20,30,40,50,60]
n = 8
p = len(l)
if n >p:
    k = n%p #8%6 = 2
else:
    k =n

print(l[p-k:]+l[:p-k])

    


