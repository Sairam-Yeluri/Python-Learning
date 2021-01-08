print ("Hello World")
x=5
y=x*2
print ("Value is", y)

print("-------------------------------------------------------------------")

print("Id of x is: ",id(x))
print("Type of x is: ",type(x))

print("-------------------------------------------------------------------")

p="sai"
print (p,x)
print()  #line space

print("-------------------------------------------------------------------")

i=10
j=10
print(id(i),id(j), "these both variables have same Id's") #Object intering. two variables have same id's

print("-------------------------------------------------------------------")


s="'Python' string"
print(s)
t = ''' "Sai" Ram'''
print(t)

print("-------------------------------------------------------------------")

l = [1,2.0,3.2,"Four","Five"]
print("This is a list:",l,"Id is",id(l))
l.append(6)
print("This is a list:",l,"Id after update is",id(l))

print("-------------------------------------------------------------------")

m = (1,2.0,3.2,"Four","Five")  #Tupple. We cant add any data to tupple
print("This is Tupple:",m," and Id is",id(m))

print("-------------------------------------------------------------------")

n = { "Name" : "Purna" , "Age" : 24 }  #Dictionary/Hashmap. saved as key and value. We cant add any value to this
print("This is Dictionary/Hashmap:", n)

print("-------------------------------------------------------------------")

o = {1,2.0,3.2,"Four","Five"}       #Sets. Cant be added new elements
print("This is a set:", o," and Id is",id(o))
