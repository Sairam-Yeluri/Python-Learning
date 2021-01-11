lst = [1,2,3,4,5,6,7,8,9]

evens = []
odds = []

for i in lst:
    if i%2==0:
        evens.append(i)
    else:
        odds.append(i)

print("Even values are {} and Odd values are {}".format(evens,odds))