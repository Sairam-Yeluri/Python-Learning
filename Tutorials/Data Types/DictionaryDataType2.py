print("CREATING DICTIONARY")
l1 = [1,2,3,4,5]
l2 = [1,4,9,16,25]
d1 = dict(zip(l1,l2))
print(d1)

print("-----------------------------------------")

l = [1,2,5]
d2 =dict.fromkeys(l,20)     #20 is assigned to all. If not specfied, null will be assigned
print(d2)
#{1: 20, 2: 20, 5: 20}

print("-----------------------------------------")

print("UPDATING DICTIONARY")
d3 = {1:1,2:4,3:9}
d4 = {4:16,5:25}
d3.update(d4)
print("Updated Dictionary is:",d3)
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

print("-----------------------------------------")

print("DELETING VALUES FROM DICTIONARY")
r1=d3.popitem()
print("List is",d3,"and randomly poped item is",r1,"(key and value)")
r2 = d3.pop(2)
print("List is",d3,"and poped item is",r2,"(only value)")
d3.clear()
print(d3)
del d3
#print(d3)   throws error because mem location of d3 is removed
