print()
def evenodd(l):
    e = 0
    o = 0
    for i in l:
        if i%2 ==0:
            e+=1
        else:
            o+=1
    return e,o

list = [1,2,3,4,5,6,7,8,9]

even,odd =evenodd(list)

print("For the list {},\nEvens are: {} and Odds are: {}".format(list,even,odd))
print()
