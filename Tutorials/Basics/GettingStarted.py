print("sai's laptop")
print('sai\'s laptop')  #\ stops the special character

print("c:\Sairam Yeluri\name")  #Raw String
print("RAW STRING:",r"c:\Sairam Yeluri\name")

print("----------------------------")


print(100,200)
print("hii")

'''Here default values for space is , and end is \n
To override them, we can specify the values'''

print(100,200, sep =",",end = " ")
print("hii")

#end="" means print on same line
#sep =","  means separate them using ","

print("----------------------------")

k = 6+3j    #  j is an imaginary number
print(type(k))

a = 2
b = 3
c = complex(a,b)
print(c,type(c))

print("----------------------------")

l= list(range(1,10))
print(l)

print("----------------------------")

k = bin(25)
print("Binary Format of is",k)

print ("Add '0b' before a binary number. we get the decimal format as:",0b11001)
print("Similarly")
print(oct(25),hex(25))

print("----------------------------")

import math as m
m.sqrt(25)

print("----------------------------")

print("Reverse Print: range(max,min,-val)")
for i in range(11,2,-2): #range(max,min,-val)
    print(i)