str = 'sairam' 

#str1 = set(str)
d ={}
for i in str:
    n = str.count(i)
    d.update({i: n})

r = min(d,key= d.get)
print(r)

print("-------------------------")

d ={}
for i in str:
    if i in d:
        d[i] +=1
    else:
        d[i] = 1
r = min(d,key= d.get)
print(r)