#Taking inputs in one line
'Traditional Method'

name = input("enter name: ")
age = input("Enter age: ")
print ("Name: ",name)
print("Age: ",age)

print("---------------------------")

name, age = input("Enter name and age(Space between them): ").split()
print ("Name: ",name)    #Sai
print("Age: ",age)      #24

print("-----------------------")

#We can do it for lists or more numbers too....
student, *marks = input("Enter students and there marks with a space gap: ").split()
print (student)     #Sai
print(marks)        #[1,2,3,4,5,6]
#* means it takes multiple values

print("--------------------------")

student, *marks,age = input("Enter students and there marks with a space gap: ").split()
#sai 10 20 30 24
print (student)     #Sai
print(age)  #24
print(marks)    #[10,20,30]

print("----------------")

name,age = input("Enter name and age: ").split(",")
#Allows input with ,
#sai,24
print ("Name: ",name)    #Sai
print("Age: ",age)      #24
