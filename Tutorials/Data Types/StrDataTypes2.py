# print(dir(str)) gives all string functions
num1 = 10
num2 = 20
print("Value of num1 is",num1,"and num2 is",num2)
print("Value of num1 is {} and num2 is {}".format(num1,num2))
print("Value of num2 is {} and num1 is {}".format(num2,num1))
print("Value of num2 is {1} and num1 is {0}".format(num1,num2))

print("--------------------------------------------------------")

s = "sairam yeluri"
print(s.capitalize())
print(s.upper())
print(s.lower())
print(s.title())
print(s.isupper())
print(s.islower()) 
print(s.istitle())

print("----------------------------------------------------------------")

# SPLIT and JOIN functions
s1 = "yeluri,purna,sai,ram"
print(s1)
s2 = s1.split(",")  #Splits string where there is a ","
print(s2)
s3 = (" ").join(s2) #Joins where there is a " "
print(s3)

print("----------------------------------------------------------")

# MAKETRANS and TRANSLATE functions
''' Creates a mapping of strings. replace it with other string'''
str1 = "abcd"
str2 = "1234"
str3 = "Python simple string abcd dbac ABCD"
table =str.maketrans(str1,str2)
result = str3.translate(table)
print(result)   #abcd is replaced by 1234

print("-------------------------------------------------------------------")

# IN, INDEX, FINd,RFIND functions
string1 = "yeluri,purna,sai,ram,sai"
print("String is:",string1)
print("sai" in string1)
print("Existing value returns:",string1.index("sai")) #only gives 1st reference position
#print(string1.index("Sai")) throws error
print("Missing value returns:",string1.find("Sai"))  #this returns -1
print("Reverse value of existing returns:",string1.rfind("sai"))  #this returns from reverse direction
print("Reverse value of missing returns:",string1.rfind("Sai"))

print("-------------------------------------------------------------------")

stng1 = "****Sairam Yeuri***-  ---///***"
print("Orginal string with stars,spaces and lines:",stng1)
stng2 = stng1.strip("*")    #Removes " " values from start and end
print("String after removing stars:",stng2)
print("Only from left hand side:",stng1.lstrip("*"))
print("Only from right hand side:",stng1.rstrip("*"))

print("-------------------------------------------------------------------")

strng1 = "Sairam"
strng2 = strng1.center(20,"*") 
print(strng2)
strng3 = strng1.ljust(20,"*")
print(strng3)
strng4 = strng1.rjust(20,"*")
print(strng4)

print("-------------------------------------------------------------------")

reg1 = "yeluri,purna,sai,ram"
reg2 = reg1.replace("sai","Saai")
print(reg2)
reg3 = reg1.replace("a","aa")
print(reg3)