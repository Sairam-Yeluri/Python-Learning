'''List are mutable
They are ordered data structures
we can store any type of data in a string
'''
l = [10,20,30,"fourty", [50,"Sixty"]]
print('''List:"''',l,'''" type is:''',type(l))

print("--------------------------------------------------------")

print(l[0]) #Indexing
print(l[-1])
print(l[-1][0])
print(l[-1][1])
#If we specify something not there, it throws an error Eg: l[20]
print(l[1:3])   #slicing
print(l[::-1])  #reversing list

print("--------------------------------------------------------")

num1 = 10
print("num1 Value is:",num1,"and id is:",id(num1))
print("First integer of list value is:",l[0],"and id is:",id(l[0]))   #Both Ids are same
print("Both Ids are same")

print("--------------------------------------------------------")

l2 = [10,20,30,40,50,60]
print("Even Values")
for value in l2[::2]:
    print(value)
print("Odd Values")
for value in l2[::-2]:
    print(value)

print("--------------------------------------------------------")

# APPEND : extends elements to list (Add list to list)
l3 = [10,20,30]
print("Before appending:",l3)
l3.append([40,50])
print("After appending:",l3)

print("--------------------------------------------------------")

# EXTEND : Add INDIVIDUAL elements to list
print("Before Extending list is:",l3)
l3.extend(["Fifty","Sixty"])
print("Extended list is:",l3)

print("--------------------------------------------------------")

#@@@@@@@@@@@@@@@@@@@@@@@@@@XXXXXXXXXXXXXXX@@@@@@@@@@@@@@@@@@@@#
print("@@@@@@@@@@@@Append and Extend Examples@@@@@@@@@@")
print("")

print("Extend Functions")
m1=[10,20,30]
print(m1)
m1.extend([40,50])
print("Adding values:",m1)
m1.extend("sai")  #          IMPORTANT
print("Adding string values:",m1)
'''
m1.extend(40)
m1.extend(40,50)
m1.extend("sai","ram")
m1.extend([60],[70])
print(m1) Throws error. Cant add 2 functions
'''
print("-----------------------------------------")
print("Append Functions")
m2 = [10,20,30]
print(m2)
m2.append(40)
print("Adding a value:",m2)
m2.append([50,60])
print("Adding a list:",m2)
m2.append(["sai","ram"])
print("Adding another list:",m2)
'''
m2.append(60,70)
m2.append([60],[70])

print(m) Throws error. Cant add 2 functions'''

print("-----------------------------------------")

print("Insert function")
print("Actual String:",l3)
l3.insert(1,800)
print("After INSERTING:",l3,'''       NOTE:"800" is inserted in 2nd position''')

print("-----------------------------------------")

print("Copy Function")
p1 = [10,20,30]
p2 =p1
print("list p1:",p1,"id is",id(p1))
print("list p2:",p2,"id is",id(p2))
print("Both has same ids")
p2.append(40)
print("After append")
print("list p1:",p1,"id is",id(p1))
print("list p2:",p2,"id is",id(p2))
'''Here p1 changes with p2
To avoid that we use copy function'''

p3 =p1.copy()
print("list p1:",p1,"id is",id(p1))
print("list p3:",p3,"id is",id(p3))
print("Both has same ids")
p3.append(50)
print("After Copy and append")
print("list p1:",p1,"id is",id(p1))
print("list p3:",p3,"id is",id(p3))
