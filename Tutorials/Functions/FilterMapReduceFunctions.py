print("Filter Function : filter(function,iterable)\n")

lst = [1,2,3,4,5,6]


#if n%2 is zero, then its an even
def iseven(n):
    return n%2==0

evens1 = list(filter(iseven,lst))
print("Function Output is:",evens1)


f = lambda n:n%2==0 

evens2 = list(filter(f,lst))
print("Lambda function output is:",evens2)


evens3 = list(filter(lambda n:n%2==0,lst))
print("Single line Lambda output is:",evens3)

print("-------------------------------------\n")

print("Map Function : Map(function,iterable)\n")

def doubles(n):
    return n*2

double1 = list(map(doubles,lst))
print("Function Output is:",double1)


f2 = lambda n:n*2

double2 = list(map(f2,lst))
print("Lambda function output is:",double2)


double3 = list(map(lambda n:n*2,lst))
print("Single line Lambda output is:",double3)

print("-------------------------------------\n")

print('''Reduce Function : from functools import reduce\n
                      reduce(function,iterable)''')

from functools import *

def addall(a,b):
    return a+b

sum1 = reduce(addall,lst)
print("Function Output is:",sum1)

f2 = lambda a,b : a+b

sum2 = reduce(f2,lst)
print("Lambda function output is:",sum2)

sum3 = reduce(lambda a,b : a+b,lst)
print("Single line Lambda output is:",sum3)








