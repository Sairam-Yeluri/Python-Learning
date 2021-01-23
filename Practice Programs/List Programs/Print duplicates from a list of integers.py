lst = [10,2,8,6,53,42,86,95,445,8,53,86,2]
lst2 = lst.copy()
st =set(lst)
uni =list(st)
print("Unique elements are: ",uni)


for x in uni:
    lst.remove(x)

print("Duplicate elements are:",set(lst))

print("---------------------------------------------")

print("List is: ",lst2)
s = []

for i in lst2:
    if lst2.count(i)>1:
        s.append(i)

print("Duplicate elements are:",list(set(s)))