'''
Mutable
All elements should be unique
immutable elements should be present in set (int,float,tuple,string)
unordered - no slising or indexing
WE CAN PERFORM UNION INTERSECTION DIFFERENCE OPERATIONS
'''
s = {10,20,30,40,50,50,30,40,20,10}
print("Addition of elements")
print("Set is",s)
s.add(80)
print("Extended Set is",s)

print("----------------------------------")

print("Functions in Sets")
s1 = {10,20,30,40,50,60}
s2 = {30,40,50,60,70,80,90}

s3 = s1.union(s2)
print("Union of two strings is",s3)

s4 = s1.intersection(s2)
print("Intersection of two strings is",s4)

s5 = s1.difference(s2)  #only elements in s1 whih are not available in s2
print("Difference of two strings is",s5)

s6 = s2.difference(s1)  ##only elements in s2 whih are not available in s1
print("Difference of two strings is",s6)

s7 = s1.symmetric_difference(s2) ##only elements in s1 and s2 that are unique
print(s7)

print("-----------------------------------------------")

print("Updating Elements")
print("")

print("Modifing base strings")
print("s1 is",s1)
print("s2 is",s2)
s1.update(s2)
print("Updated s1 is",s1)

s1.intersection_update(s2)  #All common elements in s1 and s2 are stored in s1
print("intersection_update is",s1)

s1.difference_update(s2)    #performs difference operation and updates s1
#s2.difference_update(s1) gives different result   
print("difference_update is",s1)

s1.symmetric_difference_update(s2)
print("symmetric difference_update is",s1)

k = s2.issubset(s1)
print("is it a subser:",k)
l = s2.issuperset(s1)
print("is it a superset:",l)

print("-------------------------------------")

print("Deletion of elements")
print("Set is",s1)

print("pop method")
r = s1.pop()        #Random value is poped
print("Poped Set is",s1,"and poped eement is",r)

print("remove fumction")
r2 = s1.remove(30)
print("Removed set is",s1,"and removed item is",r2,"            (wont return anything)")

print("discard method")
r3 = s1.discard(10000)
print("Removed set is",s1,"and removed item is",r3,"            (wont return anything and wont throw error for non-existing value)")

print("clear function")
s1.clear()
print("Cleared set is",s1)

del(s1)
print("Deleted set so it throws error")
print(s1)