'''
Strings are Immutable, value cant be changed.
String is ordered data structure - indexing and slicing
'''
s = "Python Simple String"
print('''String: "''',s,'''" type is:''',type(s))
#Indexing - getting a char using indexes 
print(s[0])
print(s[-1])
a = s[1]
print(a)

print("-------------------------------------------------------------------")

#Slicing - slicing a string to parts
print(s[0:6])   # from 0 to 5
print(s[7:0])   #7 to end
print(s[:6])    #Start to 5

print("-------------------------------------------------------------------")

#Stride - prints frequent character
print(s[ : :1])     #Prints a String
print(s[ : :-1])    #Reverse Print   

print("-------------------------------------------------------------------")

print(s[ : :2])     #leave print every character
print(s[ : :-2])     #leave print every character from r8 hand side

print("-------------------------------------------------------------------")

'''
indexing a outbound throws weeor while slicing throws blank
Eg: print(s[100]) is error
print(s[6:0]) throws blank
'''

for value in s[ : :2]:
    print(value)