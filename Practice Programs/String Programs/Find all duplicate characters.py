
str = "SairamYeluri"

d = []

for i in str:
   if str.count(i) > 1:
        d.append(i)
        
print("".join(set(d)))