from numpy import *
arr = (
    [1,2,3,4,5,6],
    [7,8,9,10,11,12]
)
print("Array is:",arr)

arr1 = arr.flatten()
print("Flattened array is:",arr1)

arr2 = arr1.reshape(4,3)
print("2D Reshaped Array is:",arr2)

arr3 = arr1.reshape(3,2,2)
print("2D Reshaped Array is:",arr3)

'''XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'''