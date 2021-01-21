str = "puurnnaaa"

s = set(str)
l = list(s)
l2 = "".join(l)
print(l2)

print("---------------------")

from collections import OrderedDict 

print("In Order line: ")
print("".join(OrderedDict.fromkeys(str)))

print("----------------------------")

t="" 
for i in str: 
    if(i in t): 
        pass #
    else: 
        t=t+i 
print("With Order:",t)