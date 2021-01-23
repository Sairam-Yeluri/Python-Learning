list1 = ['abc','bcd','cde','def','efg']

list2 = ['cd','de']

list3 = []
for i in list2:
    for j in list1:
        if j.find(i)>=0:
            list3.append(j)

set1 = set(list3)
print("Contains Program: ",set1)

print("-----------------------")

list4 = []
for i in list2:
    for j in list1:
        if j.startswith(i):
            list4.append(j)

set2 = set(list4)
print("Starts with Program: ",set2)