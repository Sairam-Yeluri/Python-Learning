
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))


def add_sub(x,y):
    a = x+y
    s = x-y
    return a,s

result1,result2 = add_sub(num1,num2)

print("Addition is:",result1)
print("Substraction is:",result2)

print("\n----------------------------------\n")

print("Argument Values")
def function(a,*b):     #b is a tuple value
    print("a value is:",a)
    print("b value is:",b)

function(5,10,20,"thirty")
print("")
function("five",10,20,"thirty")

print("\n----------------------------------\n")

print("Keyword Argument Values")
def fun(name,**details):
    print("Name =",name)
    print("Details =",details)
    print("\nIndividual Values are:")
    for i,j in details.items():
        print(i,j)

fun("sai",age = 24,gender="male",city="Hyderabad")

