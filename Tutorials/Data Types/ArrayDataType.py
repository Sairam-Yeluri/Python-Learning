'''
import array #or 
arr1 = array.array("i",[1,2,-3,4,5])  # 'i' (integer) accepts both positive and negative values 
'''
from array import *

arr1 = array("i",[1,2,-3,4,5])  # 'i' (integer) accepts both positive and negative values 
arr2 = array("I",[1,2,3,4,5]) # 'I' wont accept negative value

arr3 = array("f",[2,3,4.1,-5.1])
arr4 = array("d",[2,3,4.1,-5.1])

arr5 = array("u",['a','b','c','d','e'])

print("Integer",arr1)
print("Non negative integer",arr2)
print("Float",arr3)
print("Double",arr4)
print("Character",arr5)


print("---------------------------------")

print("Buffer of array is:",arr1.buffer_info(),"                  tupple(Address,size)")

print("Type of array is:",arr1.typecode)

arr1.append(6)
print("Appended array is:",arr1)

arr1.remove(6)
print("Removed array is:",arr1)

arr1.reverse()
print("Reversed array is",arr1)

print("First value is:",arr1[0])

print("Individual values of array is: ")
for k in range(len(arr1)):
    print(k,"th value of array is:",arr1[k])

print("")

for k in arr1:
    print(k)

newArr1 = array.array(arr1.typecode, (a for a in arr1))
print("Copied array is:",newArr1)