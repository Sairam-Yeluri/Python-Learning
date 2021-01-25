dic = {'month' : [1, 2, 3], 'name' : ['Jan', 'Feb', 'March']}

k = list(dic.values())
print(k)

key = k[0]
val = k[1]

dic2 = dict(list(zip(key,val)))

print("New Dictionary is: ",dic2)

print("----------------------")

res = dict(zip(dic['month'], dic['name']))
print(res)