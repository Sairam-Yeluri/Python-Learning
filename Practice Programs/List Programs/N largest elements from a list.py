lst = [10,2,8,6,53,42,86,95,445]
print("Original list is:")
print(lst)

l =len(lst)

n = int(input("Enter the number(less than {}): ".format(l)))

lst.sort()
print("Sorted list is:")
print(lst)

print("Last {} elements in the list is:".format(n))
print(lst[l-n:l:1])

print("\nor")

print("lst[-n:] : ",lst[-n:])