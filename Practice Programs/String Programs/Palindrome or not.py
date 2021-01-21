str1 = "ss"
str2 =str1[::-1]

if str1==str2:
    print("Yes")
else:
    print("No")

print("----------------------------------------\n")

str3 = ''.join(reversed(str1))
'''str4 = reversed(str1)
print(str4)'''
if str3 == str1:
    print("Yes")
else:
    print("No")

