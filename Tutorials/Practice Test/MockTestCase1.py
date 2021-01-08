k = 1
l = []
print("Empty List is",l)
while k == 1:
    val = input("Enter value:")
    if val == "q":
        k = 2
    else:
        fval = float(val)
        print(fval,type(fval))
        l.append(fval)
print("Runners list is",l)
s = set(l)
l2 = list(s)
l2.sort()
print("Sorted list is",l2)
if len(l2)>=4:
    print(l2[1])
    print(l2[2])
    print(l2[3])
else:
    print("insufficient data")
    