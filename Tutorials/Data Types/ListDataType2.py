'UPDATE and DELETE operations'

l = [10,80,20,30,30,40,50]

#    update
print("Actual list is:",l)
l[1] = 20
print("Updated list is:",l)
#[10, 20, 20, 30, 30, 40, 50]

print("-----------------------------------------")

'''For delete, we have POP, REMOVE, CLEAR, DEL functions'''

#       pop is used on the bases of positions
print("pop Function")
print("Orginal list is:",l)
r1 = l.pop()     # REMOVES last element and store in r
print("New List is:",l,"and (last) removed item r is:",r1)
r2 = l.pop(2)
print("New List is:",l,"and removed item r is:",r2)

print("-----------------------------------------")
#       remove is used on the bases of value
print("remove Function")
print("Orginal list is:",l)
r3 = l.remove(30)       #Removes only one elemet at a time
print("New List is:",l)

print("-----------------------------------------")
#       clear is used to remove all elements
print("clear Function")
print("Orginal list is:",l)
l.clear()
print("cleared List is:",l)

print("-----------------------------------------")
#       del is used to delete memory location
print("del Function")
l1 = [10,20,30]
print("Orginal list",l1,id(l1))
del l1
'''print("cleared List is:",l,id(l1))  
As there is no mem location, it throws an error'''

print("-----------------------------------")

l2 = [50,43,85,76,15]
print("sort function")
print("Orginal list is:",l2)
l2.sort()
print("Sorted list is:",l2)
'print(l2.sort())    nothing Returns'

print("--------------------------")

print("reverse function")
l2.reverse()
print("Reverse list:",l2)
'''
print(l2.reverse())     nothing Returns
 k= l2.sort() and m=l2.reverse() and printing k,m wont work as they wont return anything
to return, we use sorted function
'''

print("--------------------------")

print("sorted function (Works on any data type)")
l3 = [50,43,76,85,76,15]
l4 = sorted(l3)
print("Actual list is",l3)
print("Sorted list is",l4)

print("--------------------------")

print("index function")
print("Index is",l4.index(76))
#Index is 3 (position)

print("--------------------------")

print("count function")
print("count is",l4.count(76))

print("--------------------------")

print("concatinate function")
print("concatinated is is",l3+l4)

'''This wont modift l3 or l4 like extend and append.
Here we can assign l3+l4 to l5'''

print("--------------------------")

print("otherXXX function")
l5 = [1]
print("10 times is",l5 * 10)