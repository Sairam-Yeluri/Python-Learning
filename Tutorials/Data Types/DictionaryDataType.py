'''
Also called as HashMap
Specified by KEY and VALUE pair
these are mutable: #CAN EDIT DATA
these are unordered: cant do SLICING and INDEXING
key should be unique
keys is immutable'''

d1 = {"id":1423199,"name":"sai","email":"sairam.com"}
print(d1)
d2 = {"id":1423199,"name":"sai","email":"sairam.com","name":"sairam"}
print(d2)   #Name updated automaticallt

print("-------------------------------------------")

print("Adding a value")
d2["contact"] = 9492492404
print("Updated d2 is",d2)

print("-------------------------------------------")

print("print a specific value")
print(d2["name"])   #cant do it as d2[0] or d2[1] if we give, it throws error

print("-------------------------------------------")

print("get function")
print(d2.get("empid"))      #if the key value is not there, it wont throw error
print(d2.get("empid","Not available@@@"))      #this time it returns the specified value

print("-------------------------------------------")

print(d2.setdefault("age",24))     #creates a new key and set default value to specified value
print(d2)

print("-------------------------------------------")

print("Iteratin values")
for x in d2:
    print(x,"and",d2[x])    #we get key and values.

print("-------------------------------------------")

# KEY VALUE and ITEMS
print("Keys are",d2.keys())
print("Values are",d2.values())
print("Items are",d2.items())

print("-------------------------------------------")

# ITERATE OVER ITEMS
for t in d2.items():
    print(t)