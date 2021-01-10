# NORMAL FUNCTION

n = 5
def square(a):
    print(a,"square is",a*a)

square(n)

print("--------------------------------------")

f = lambda a: a*a

print("square of",n,"is",f(n))

print("---------------------")

f = lambda x,y : x+y

print("Sum is: ",f(4,3))