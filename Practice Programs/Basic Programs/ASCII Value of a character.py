print("Program to print ASCII Value of a character\n")

char = input("Enter the character: ")

if len(char)>1:
    print("ASCII value of only",char[0], "(first character)is calculated")
    c = char[0]
else:
    c = char

print("ASCII value of" ,c,"is",ord(c))