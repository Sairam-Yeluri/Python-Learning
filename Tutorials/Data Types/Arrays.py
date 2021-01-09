import array
arr1 = array.array("i",[1,2,-3,4,5])  # 'i' (integer) accepts both positive and negative values 
arr2 = array.array("I",[1,2,3,4,5]) # 'I' wont accept negative value

arr3 = array.array("f",[2,3,4.1,-5.1])
arr4 = array.array("d",[2,3,4.1,-5.1])

print("Integer",arr1)
print("Non negative integer",arr2)
print("Float",arr3)
print("Double",arr4)

print("---------------------------------")

print("Buffer of array is:",arr1.buffer_info(),"                tupple(Address,size)")
'''We have append, remove, reverse functions'''