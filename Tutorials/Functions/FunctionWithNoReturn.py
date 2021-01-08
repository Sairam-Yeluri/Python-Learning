#Defining Function
def rev_val(value):
    revere = value[::-1]
    print("Reverse of value is",revere)

#Calling Function

print("If the input is String")
s = "sairam"
#rev_val(s)  This wont return anything (none)
k = rev_val(s)  #We called the function. so it prints here
print("Returned value is",k)

print("--------------------------")

print("If the input is list")
s1 = [10,20,30,40,50]
rev_val(s1)