a = ["sai","ram","Yeluri"]
l = len(a)
a2 =[]
for i in range(l-1,-1,-1):
    a2.append(a[i])

print(a2)

a.reverse()
print(a)
