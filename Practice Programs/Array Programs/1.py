print("Python Program to find sum of array\n")

l = [10,20,30,40,50,60]
sum = 0
for i in l:
    sum = sum + i
print("Sum of array is",sum)

print("------------------------------")


def sum(k):
    sum = 0
    for i in k:
        sum = sum + i
    return sum


p = sum(l)
print("Sum of elements is",p)
