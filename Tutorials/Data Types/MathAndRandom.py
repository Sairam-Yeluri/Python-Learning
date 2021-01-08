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
print(sum(l1))
# But the expected output is 1
#So we use math functions
print('''Math Functions
For math functions, we have to import math''')
import math
print("Math sum is",math.fsum(l1))

num = 15.5368
#To get uper and lower limits
print("Upper value of", num,"is",math.floor(num),"and lower value is",math.ceil(num))

print("Squareroot",math.sqrt(25))

print("Power",math.pow(10,2))

print("Factorial",math.factorial(5))

d,i = math.modf(num)
print("modf function decimal is",d,"integer is",i)

print("log value",math.log(10))   #default is 'e'
print("log value",math.log(10,2))
# The above function can be written as
print("log 10 to the base  is",math.log2(10))

print("Trignomentry",math.sin(math.radians(30)))    #Convert degrees to radians

print("-----------------------------------------------")

print('''Random Function
for using random functions, we import random''')
import random
print("Random number(between 0 and 1)",random.random())

l = [1,2,3,4,5,6]
print("Random number from choice is",random.choice(l))

print("Randint function",random.randint(10,100),"           (Prints a number in specified range)")

print("Randrange function",random.randrange(1,3),"           (Prints a number in specified range except the last one)")

print("Randon floating point number (uniform)",random.uniform(1,3))