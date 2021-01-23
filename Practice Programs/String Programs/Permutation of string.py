from itertools import permutations 

str = 'sai'

str2 = permutations(str)

for i in str2:
    print("".join(i))

print("------------------------------")

str3 = permutations(str)
d = []
for i in str3:
    if i not in d:
        d.append(i)
        print("".join(i))