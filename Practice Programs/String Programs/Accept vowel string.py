str = input("Enter string: ")

vowels = 'aeiouAEIOU'
temp = 0
l = len(str)

for i in str:
    if vowels.find(i) >=0:
        temp +=1
print("Number of Vowels are: ",temp)
if l == temp:
    print("It has some vowels")
else:
    print("This is Vowel Free")