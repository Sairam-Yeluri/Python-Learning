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
k =m.sqrt(25)
print("Squareroot is: ",k)

print("----------------------------")

print("Reverse Print: range(max,min,-val)")
for i in range(11,2,-2): #range(max,min,-val)
    print(i)

print("----------------------------")

a = 10  #Global Variavle
b = 20
def something():
    a =15   #Local Variable
    c = 20
    print("in Function a value is:",a)
    print("in Function b value is:",b)
    print("in Function c value is:",c)


print("Out of function before calling function",a)    #Out of the function

something() #Prints Local Variable
print("Out of function after calling function",a)    #Prints Global Variable
#print("Out of  Function c value is:",c)  We cant use local as global

print("----------------------------")

k = 10
def otherthing():
    global k
    global m
    k = 20
    m = 30
    print("In function k is:",k)
    print("In function m is:",m)

otherthing()
print("Out of function k is:",k,"      k value changed here also")
print("Out of function m is:",m,"      m value is used globally and created")

print("----------------------------")

print("Format Function")
num1 = 10
num2 = 20

print("num1 is {} and num2 is {}".format(num1,num2))

print("----------------------------")

import sys
print("Recursion limit is: ",sys.getrecursionlimit())

sys.setrecursionlimit(10)
print("After setting, Recursion limit is: ",sys.getrecursionlimit())

