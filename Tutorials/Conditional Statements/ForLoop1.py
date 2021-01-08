#For loop part 1
'''for Variable_Name in Iterable_Datatype:
    statement
    '''
#What are iterable datatypes: string, list, tupple, dictionary, set
l = [10,20,30,40,50,60]
for x in l:
    print (x)

print("-------------------------------------------------------------------")

#addition of all variables
sum = 0
for x in l:
    sum = sum+x
    print ("Inside intendation value is:",sum)
print("Total sum is:",sum)

l1 = range(5)   #from 0 to n-1
l2 = range(5,10)   #from n to m-1
l3 = range(1,10,2)  #from n to m-1 leaving every o

for l1 in range(5):
    print(l1)
print()
for l2 in range(5,10):
    print(l2)
print()
for l3 in range(1,10,2):
    print(l3)