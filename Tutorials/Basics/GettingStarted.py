print("sai's laptop")
print('sai\'s laptop')  #\ stops the special character

print("c:\Sairam Yeluri\name")  #Raw String
print("RAW STRING:",r"c:\Sairam Yeluri\name")

print("----------------------------")


print(100,200)
print("hii")

'''Here default values for space is , and end is \n
To override them, we can specify the values'''

print(100,200, sep =",",end = " ")
print("hii")

k = 6+3j    #  j is an imaginary number
print(type(k))

a = 2
b = 3
c = complex(a,b)
print(c,type(c))

l= list(range(1,10))
print(l)