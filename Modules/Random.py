'''Random Function
For using random functions, we import random'''
print()

from random import *
print("Random number(between 0 and 1)",random())
#any random from 0 to 1

l = [1,2,3,4,5,6]
print("Random number from choice is",choice(l))
# any random in l

print("Randint function",randint(10,100))
#Prints a number in specified range

print("Randrange function",randrange(1,3))
#Prints a number in specified range except the last one

print("Randon floating point number (uniform)",uniform(1,3))
#Randon floating point number

lst = ['a','b','c','d']
cho = choice(lst)
print("Random Choice value is: ",cho)