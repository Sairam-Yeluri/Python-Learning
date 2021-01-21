str = "Purna Sai Ram Yeluri"

str2 = str.split(" ")

even = []
odd = []
for i in str2:
    if len(i)%2 ==0:
        even.append(i)
    else:
        odd.append(i)


print("\nEvens are:")
for i in even:
    print(i)

print("\nOdds are:")
for i in odd:
    print(i)