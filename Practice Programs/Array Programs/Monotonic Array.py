print("Python Program to check if given array is Monotonic")

'''Given an array A containing n integers. The task is to check whether the array is Monotonic or not. An array is monotonic if it is either monotone increasing or monotone decreasing.
An array A is monotone increasing if for all i <= j, A[i] <= A[j]. An array A is monotone decreasing if for all i <= j, A[i] >= A[j].'''

l1 = [10,20,30,40]
l2 = [40,30,20,10]
l3 = [5.7,2,9]

l = len(l1)
k1 = 0
k2 = 0

for i in range(0,l-1):
    if (l1[i]>l1[i+1]):
        k1 = k1+1
    if (l1[i]<l1[i+1]):
        k2 = k2+1


if (k1==l-1 or k2 ==l-1):
    print("Yes")
else:
    print("No")
print("-------------------------------\n")

def mono(arr):
    result = False
    k1 = 0
    k2 = 0
    ln = len(arr)
    for i in range(0,ln-1):
        if (arr[i]>arr[i+1]):
            k1 =k1+1
        if (arr[i]<arr[i+1]):
            k2 = k2+1
    if k1 == ln-1 or k2 == ln-1:
        result = True
    return result

p = mono(l1)
print(p)

