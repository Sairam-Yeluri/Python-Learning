'''Random Function
For using random functions, we import random'''
print()

from random import *
print("Random number(between 0 and 1)",random())
#any random from 0 to 1

lst = [1,2,3,4,5,6]
print("Random number from choice is",choice(lst))
# any random in lst

print("Randint function",randint(10,100))
#Prints a number in specified range (as a 6 sided die)

print("Randrange function",randrange(1,3))
#Prints a number in specified range except the last one

print("Randon floating point number (uniform)",uniform(1,3))
#Randon floating point number

lst = ['a','b','c','d']
cho = choice(lst)
print("Random Choice value is: ",cho)

lst = ['a','b','c','d']
code = choices(lst,k=6)
print(code)    #randomly choose values from list 
code2 = choices(lst,weights=[4,4,2],k=10)
print(code2)    #Weights means probability
code3 = choices(lst,weights=[4,4,1],k=10)
print(code3)

nums = list(range(1,10))
print(nums)
shuffle(nums)
print(nums)

deck = list(range(1,53))
print(sample(deck,13))
