from itertools import *
dic = {'a':[1,2],'b':[3,2],'c':[3,2,4]}

k = dic.values()
print("Dictionary values: ",k)

k1 = chain(dic.values())
print("Chain Values: ",k1)

k2 = list(chain(dic.values()))
print("Listed Chain Values: ",k2)

k3 = list(chain(*dic.values()))
print("Listed Chain Values in single string : ",k3)

s = set(k3)
print(s)
l = list(s)
print(l)
l.sort
print(l)

print("--------------------")

dic = {'a':[1,2],'b':[3,2],'c':[3,2,4]}

k = list(dic.values())
lst = []
print(k)
for i in k:
    for j in i:
        lst.append(j)
print(lst)

s = list(set(lst))
print(s)

