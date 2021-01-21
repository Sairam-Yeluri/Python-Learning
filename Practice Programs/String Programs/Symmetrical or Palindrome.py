str1 = "khokho"
str2 = "amamama"

def find(str):
    l = len(str)
    if l%2 ==0:
        mid = (l//2)
    else:
        mid = (l//2) +1
    s1 = str[::-1]
    s2 = str[0:mid]
    s3 = str[mid : l]
    if str == s1:
        return "Pallindrome"
    elif s2==s3:
            return "Symmentrical"
    else:
        return "None"

k1 = find(str1)
print("{} is {}".format(str1,k1))
k2 = find(str2)
print("{} is {}".format(str2,k2))
