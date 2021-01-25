#Arthematic +,-,*,/,//,**,%
num1 = 4
num2 = 2
print(num1+num2)
print(num1-num2)
print(num1*num2)
print(num1/num2)
print(num1**num2)   #power
print(num1//num2)   #divisor
print(num1%num2)    #reminder

print("-------------------------------------------------------------------")

#Comparision <,>,<=,>=,==,!=
print(num1>num2)
print(num1<num2)
print(num1>=num2)
print(num1<=num2)
print(num1==num2)
print(num1!=num2)

print("-------------------------------------------------------------------")

#Identity Operators:  is,is not (Compare Memory Location)
p = 3
q = 2
l1 = [10,20,30]
l2 = [10,20,30]
print (p == q)
print (p is q)
print (p is not q)
print (l1 == l2)
print(l1 is l2)  #There mem location is different
print(l1 is not l2)

print("-------------------------------------------------------------------")

#Assignment Operators =, +=, -=, *=, /=
num3 = 100
num3 += 5
print(num3)
num3 -= 5
print(num3)
num3 *= 5
print(num3)
num3 /= 5
print(num3)

print("-------------------------------------------------------------------")

#BitWise Operators &,|,^,>>,<<
num4 = 2
num5 = 1
print(bin(num4),"",bin(num5))
print(num4 & num5)
print(num4 | num5)
print(num4 ^ num5)
print(num4 >> 1)    #shift bits righthand side by 1
print(num4 << 1)    #shift bits lefthand side by 1

print("-------------------------------------------------------------------")

#logicalOperators and, or ,not

print((10 == 10) and (20 == 20))
print((10 == 10) or (20 == 30))
print(10==10)
print(not(10==10))
print(not(10==20))

print("-------------------------------------------------------------------")

#MembershipOperators in, not in

l = [10,20,30,40,50]
print(30 in l)  #True
print(90 in l)  #False

s= "Sairam Yeluri"
print("s" in s)     #False
print("Sairam" in s)    #True
print("t" in s)     #False