print()
lst = [19,82,3,41,52,16,17,84,69]
small = lst[0]
large = lst[0]

for i in lst:
    if i>large:
        large = i

print("Large value is:",large)

for i in lst:
    if i<small:
        small = i

print("Small value is:",small)

print("------------------------------------------\n")

lst.sort()
print("Large value is:",lst[len(lst)-1])
print("Small value is:",lst[0])
