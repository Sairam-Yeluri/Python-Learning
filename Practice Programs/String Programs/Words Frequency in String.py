str = 'sai ram is sai ram' 

str1 = str.split(" ")
d ={}
for i in str1:
    n = str1.count(i)
    d.update({i: n})

for i in d:
    print("{} : {}".format(i,d[i]))
