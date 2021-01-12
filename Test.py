def fact(n):
    result = n
    if n<1:
        return "invalid number"
    elif n==0 or n==1:
        return 1
    else:
        result = result * fact(n-1)
        return result

k = fact(3)
print(k)