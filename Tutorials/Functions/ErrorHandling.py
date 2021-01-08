#Defining Function
def rev_val(value):
    reverse = value[::-1]
    return reverse


#Calling Function

print("If the input is Number")
s = 100
#k = rev_val(s)  
#print("Returned value is",k)   
print("THROWS an ERROR because of non repeting value")

print("-------------------------------------------")

#To remove that:

def rev_val2(val):
    if ((type(val) ==list) or (type(val) ==str)):
        reverse = val[::-1]
        return reverse
    else:
        temp = str(val)
        reverse = temp[::-1]
        return reverse

#Calling Function

s = 100
k = rev_val2(s)
print("Returned value is",k)