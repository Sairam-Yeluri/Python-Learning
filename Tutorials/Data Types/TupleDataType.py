''' tuple is immutable and ordered
se we cant add/delete values
But it supports indexing and slicing '''
t = (10,20,20,30,40,40,50) 
print("Tuple :",t)  #INDEXING and SLICING

print("---------------------------------")

l=t.index(20)
print("Index of 20 is:",l)

print("---------------------------------")

m = t.count(20)
print("Count of 20 is:",m)

print("---------------------------------")

'''Tuple is used while passing data from one function to another function'''

for index,value in enumerate(t):
    print(index,value)

#This we can write as
print("Using tuple")
for t1 in enumerate(t):
    print (t1)
print("All the indexes")
for t1 in enumerate(t):
    print (t1[0])
print("All the values")
for t1 in enumerate(t):
    print (t1[1])