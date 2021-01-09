#For loop part 2
# Break, Continue, enumerate
#Break
l = [10,20,30,40,50,60,70,80]
key = 500
for x in l:
    if x == key:
        print("Element","'",x,"'","Found")
        break
    else:
        continue
else:
    print("Element not found")
print("Process Complete")

print("-------------------------------------------------------------------")

for index,value in enumerate(l):
    print(index,value)

print("-------------------------------------------------------------------")

print("Odd positions are:")
for index,value in enumerate(l):
    if index%2==0:
        print(value)
    else:
        continue

print("-------------------------------------------------------------------")

print("Even positions are:")
for index,value in enumerate(l):
    if index%2!=0:
        print(value)
    else:
        continue

print("-------------------------------------------------------------------")

for x in l:
    if x == key:
        print("Element","'",x,"'","Found")
        break
    else:
        pass
        '''If there is no condition. Then we write pass.
        Code after 'Pass' will execute everytime.'''

print("-------------------------------------------------------------------")

e =30
for x in l:
    if x%e ==0:
        print("Element Found",x) #Returns 'first found' statement that is divisible by 30
        break
else:
    print("Element Not Found")

print("Bye")

print("")

e2 = 90
for x in l:
    if x%e2 ==0:
        print("Element Found",x) 
        break
else:
    print("Element Not Found")  #Returns no value only when elemengt not found

print("Bye")
