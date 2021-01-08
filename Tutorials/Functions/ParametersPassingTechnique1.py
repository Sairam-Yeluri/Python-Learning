print("Positional Argument")

#Program to find value in a list
def find_value(l,k):
    for v in l:
        if v == k:
            return True
        else:
            pass
    else:
        return False 

#calling Function
l = [10,20,30,40,50]
k = 400
r = find_value(l,k) 
print(k,"is present in list:",r)

r1 = find_value(l,20) 
print("Defined value is present in list:",r1)

print("--------------------------------")

print("Default Argument")

#Program to generate password
import random
def gen_pwd(len = 8):
    l = ["@","#","$","%","&"]
    upper = chr(random.randint(65,90)) #A to Z
    lower = chr(random.randint(97,122)) #a to z
    spcl = random.choice(l)
    num = random.randint(10000,99999)

    pwd = upper + lower+ spcl + str(num)
    s = random.sample(pwd,len)  #Trims sample to specified length
    password = ("").join(s)
    return password

#calling Function
password1 = gen_pwd()
print("default password is:",password1)

password2 = gen_pwd(5)
print("specified password is:",password2)

print("---------------------------------------")

print("Keyword Argument")

#Program to validate Username and password
def validate(username,password):
    s = {"sai":123, "ram":456, "yeluri":789}
    pwd = s.get(username)
    if pwd == password:
        return "Login Success"
        
    else:
        return "Login Failed"
    

#Calling Function
k = validate("sai",123) #Ordered
print("Ordered function:",k)

k2 = validate(password=456,username="ram")
print("Unordered Function:",k2)

