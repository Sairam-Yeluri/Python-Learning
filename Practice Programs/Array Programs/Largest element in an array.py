print("Python Program to find largest element in an array\n")

l = [10,20,30,40,50,60]

print("max value is",max(l))

print("------------------------------\n")

val = 0
for i in l:
    if i>val:
        val = i

print("Max value is",val)
    
