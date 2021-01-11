l = [1,2,3,4,5,6]
print("Original list is:",l)
s =len(l)

n1 =l[0] 
l [0]=l[s-1]
l [s-1]=n1
print("Updated list is:",l)

print("----------------------------")

newList = [1,2,3,4,5,6]
print("Original list is:",newList)
newList[0], newList[-1] = newList[-1], newList[0] 
print("Updated list is:",newList)

print("----------------------------")

def swaplist(lst): 
      
    first = lst.pop(0)    
    last = lst.pop(-1) 
      
    lst.insert(0, last)   
    lst.append(first)    
      
    return lst
      
newList = [12, 35, 9, 56, 24] 
print("Original list is:",newList)
print("Updated  list is:",swaplist(newList)) 