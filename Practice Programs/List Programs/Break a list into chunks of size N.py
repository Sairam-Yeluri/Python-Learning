lst = [1,2,3,4,5,6,7,8,9]
n = 3
print("Original list is:",lst)

x = [lst[i:i + n] for i in range(0, len(lst), n)]  
print("Nw List is:",x) 

print("or")
lst2 =[]
for i in range(0, len(lst), n):
    p = lst[i:i + n]
    lst2.append(p)

print("Nw List is:",lst2) 

        
