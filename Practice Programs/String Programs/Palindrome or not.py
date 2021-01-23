str1 = "sasi"
str2 =str1[::-1]

if str1==str2:
    print("Yes")
else:
    print("No")

print("----------------------------------------\n")

'''str = reversed(str1)
print(str)'''
str3 = ''.join(reversed(str1))
print("Reversed string is: ",str3)

if str3 == str1:
    print("Yes")
else:
    print("No")

