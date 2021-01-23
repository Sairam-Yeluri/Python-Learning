lst = ["sai","ram","Yeluri"]
l = len(lst)
lst2 =[]
for i in range(l-1,-1,-1):
    lst2.append(lst[i])

print("Original list: ",lst)
print("Reversed list: ",lst2)

print("---------------------------")

print("Original list: ",lst)
lst.reverse()
print("Reversed list: ",lst)
