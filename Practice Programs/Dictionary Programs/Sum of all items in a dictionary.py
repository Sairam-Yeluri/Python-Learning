dic = {'a':[1,2],'b':[3,2],'c':[3,2,4]}

k = list(dic.values())
lst = []
sum = 0
print(k)
for i in k:
    for j in i:
        sum = sum + j

print('sum of all items is:',sum)