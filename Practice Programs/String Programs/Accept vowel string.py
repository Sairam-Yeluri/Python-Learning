str = input("Enter string: ")

vowels = 'aeiouAEIOU'
temp = 0
l = len(str)

for i in str:
    if vowels.find(i) >=0:
        temp +=1
#print(temp)
if l == temp:
    print("Yes")
else:
    print("No")