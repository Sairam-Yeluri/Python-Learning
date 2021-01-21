def binary(str):
    k = 1
    for i in str:
        if i=='0' or i=='1':
            pass #
        else:
            k = 2
    if k == 1:
        print("True")
    else:
        print("False")

s1 = '10011100'
s2 = '10050010'

binary(s1)
binary(s2)
