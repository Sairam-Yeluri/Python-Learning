print ("Hello World")
x=5
y=x*2
print ("Value is", y)

print("-------------------------------------------------------------------")

print("Id of x is: ",id(x))
print("Type of x is: ",type(x))

print("-------------------------------------------------------------------")

p="sai"
print (p,x)
print()  #line space

print("-------------------------------------------------------------------")

i=10
j=10
print(id(i),id(j), "these both variables have same Id's") #Object intering. two variables have same id's

print("-------------------------------------------------------------------")


s="'Python' string"
print(s)
t = ''' "Sai" Ram'''
print(t)

print("-------------------------------------------------------------------")

l = [1,2.0,3.2,"Four","Five"]
print("This is a list:",l,"Id is",id(l))
l.append(6)
print("This is a list:",l,"Id after update is",id(l))

print("-------------------------------------------------------------------")

m = (1,2.0,3.2,"Four","Five")  #Tupple. We cant add any data to tupple
print("This is Tupple:",m," and Id is",id(m))

print("-------------------------------------------------------------------")

n = { "Name" : "Purna" , "Age" : 24 }  #Dictionary/Hashmap. saved as key and value. We cant add any value to this
print("This is Dictionary/Hashmap:", n)

print("-------------------------------------------------------------------")

o = {1,2.0,3.2,"Four","Five"}       #Sets. Cant be added new elements
print("This is a set:", o," and Id is",id(o))

print("-------------------------------------------------------------------")

import array
arr1 = array.array("i",[1,2,-3,4,5])  # 'i' (integer) accepts both positive and negative values 

print("Array is: ",arr1)

print("-------------------------------------------------------------------")

k = bin(25)
print("Binary Format of is",k)

print ("Add '0b' before a binary number. we get the decimal format as:",0b11001)
print("Similarly")
print(oct(25),hex(25))
