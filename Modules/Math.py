'''print(dir(__builtins__))
help(__builtins__)
print(dir(math))
help(math)'''

l = [100,200,300,400,500,600]

print("Genral Functions")
print("Sum is",sum(l))
print("Max is",max(l))
print("Min is",min(l))

num1 = 25.55341241254552
num2 = 25.45553345854212
print("Roundoff of num1 is",round(num1),"and num2 is",round(num2))
print("Roundoff upto 2 decimals is",round(num1,2),"and",round(num2,2))

print("---------------------------------------")

l1 = [0.1] * 10
print(l1)
#[0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
print(sum(l1))
#0.999999999
'''But the expected output is 1
So we use math functions'''
print('''Math Functions
For math functions, we have to import math''')

from math import *
print("Math sum is",fsum(l1))
#1.0

num = 15.5368
#To get uper and lower limits
print("Upper value of", num,"is",floor(num),"and lower value is",ceil(num))

print("Squareroot",sqrt(25))

print("Power",pow(10,2))

print("Factorial",factorial(5))

print(" GCD of two number 60 and 48 is ", gcd(60, 48))      #only in some compilers



d,i = modf(num)
print("modf function decimal is",d,"integer is",i)
#num = 15.5368   d = 0.5368  i = 15


print("log value",log(10))   #default is 'e'
print("log value",log(10,2))
# The above function can be written as
print("log 10 to the base  is",log2(10))

print("Trignomentry",sin(radians(30)))    #Convert degrees to radians

