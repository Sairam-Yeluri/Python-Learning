num1 = input("Enter num1:")
num2 = input("Enter num2:")
z=num1 + num2
print("String value is",z)    #by default x and y and z will be string

print("-------------------------------------------------------------------")

a = int(num1)
b = int(num2)
z= a+b
print("Numeric value is",z)

print("-------------------------------------------------------------------")

#or we can write
p = int(input("Enter p:"))
q = int(input("Enter q:"))
r = p+q
print("Value r is",r)
print("Value (p+q) is",p+q)

print("-------------------------------------------------------------------")

'''@@@@@@@@@@@@@@@@@@Character in Python @@@@@@@@@@@@@@@@@@@@@@@'''

print("-------------------------------------------------------------------")

ch = input("Enter character:")
print("Direct Print",ch)
print("Character Print",ch[0])

print("-------------------------------------------------------------------")

ch2 = input("Enter character:")[0]
print("Character print in 2nd way",ch2)

print("-------------------------------------------------------------------")

'''Take a List as input'''

lst=[]
lst =map(int,input().split())
lst2=list(lst)
print(lst)
print(lst2)

print("-------------------------------------------------------------------")

#Expression value
value = eval(input('''Enter Expression like "2+3-1":'''))
print("Expression result is",value)
