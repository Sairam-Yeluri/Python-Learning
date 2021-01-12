lst = [10,2,8,6,53,42,86,95,445,8,53,86,2]
st =set(lst)
lst2 =list(st)
print("Unique elements are: ",lst2)


for x in lst2:
    lst.remove(x)

print("Duplicate elements are:",set(lst))

print("or")

print("Duplicate elememts are:",set([i for i in lst if(lst.count(i)>0)]))

'''p = {}
for i in lst:
    if(lst.count(i)>0):
        p.append(i)
print(p)
'''

    

