str = "sai is best . sai also knows python. sai can write programs on python."
print("")
print("The original string is : " + str)
  
# initializing replace mapping  
dict = {'sai' :  'He', 'python.' : 'It.' } 
  
# Replace duplicate Occurrence in String 
# Using split() + enumerate() + loop 
test_list = str.split(' ') 
res = set() 
for idx, ele in enumerate(test_list): 
    if ele in dict: 
        if ele in res: 
            test_list[idx] = dict[ele] 
        else: 
            res.add(ele) 
res = ' '.join(test_list) 
  
# printing result 
print("") 
print("The string after replacing : " + res) 
print("")
