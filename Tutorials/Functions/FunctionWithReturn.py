#Defining Function
def rev_val(value):
    reverse = value[::-1]
    return reverse

#Calling Function

print("If the input is String")
s = "sairam"
k = rev_val(s)  #Return value is stored in k
print("Returned value is",k)
print("")
#If we try to print function output, it will returns same
print("Output of function is",rev_val(s),"      (Same as above)")

print("-------------------------------------------")

print("If the input is list")
s1 = [10,20,30,40,50]
k1 = rev_val(s1)
print("Returned value is",k1)
print("")
print("Output of function is",rev_val(s1),"      (Same as above)")
#rev_val(s1)