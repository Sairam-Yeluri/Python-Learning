str1 = 'sai ram YeLurI'
str2 = 'SaI raM YEluRi'

l = []
for i in str1:
    if (str2.find(i)>=0 and i != " "):
        l.append(i)

s = set(l)  #Remove duplicates
l2 = list(s)  #Again to string
l2.sort()   #Sorting in assending order

print("\nCount is {} and Matching items in str1 are: ".format(len(l2)))
for i in l2:
    print(i)

print("\n------------------------\n")

s1 = set(str1)
s2 = set(str2)

s3 = s1 & s2   #Intersection

s4 = list(s3)

print(s1,s2,s3,s4)

s4.sort()
print("\nCount is {} (including space) and Matching items in str1 are: ".format(len(s4)))
for i in s4:
    print(i)
