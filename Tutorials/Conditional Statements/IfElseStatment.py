#if Block
'''
if [Condition 1]:
    Statment 1
elif [Condition 2]:
    Statment 2
else:
    FinalCondition
'''
num1 = 10
num2 = 20

if num1>num2:
    print(num1,"is Bigger")
elif num1<num2:
    print(num2,"is Bigger")
else:
    print("Both are same")

print("\n----------------------------\n")

if 1:       #Opposite is 0,None
    print("If is printed")
else:
    print("Else is printed")

print("\n----------------------------\n")

if 'a':     #Opposite is 0,None
    print('''String "a" is also considered''')
else:
    print("a is not considered")
