print("Variable length positional Argument")

def testadd_value(*args):   #Converts values to tuple
    print("Arguments are",args)

testadd_value(10,20,30,40,"sai")

print("")

def add_value(*l):
    lst = []
    for k in l:
        lst.append(k)
    return lst

result1 = add_value(10,20,30)
print(result1)

result2 = add_value(40,50,60,"Seventy")
print(result2)

print("-------------------------------------")

print("Variable length Keyword Argument")

def get_details(**kwarg):
    print("Keyword arguments are",kwarg)

get_details(name="sai", email = "sai@yeluri.com", age = 24, dob = "08-02-1997")

print("")

