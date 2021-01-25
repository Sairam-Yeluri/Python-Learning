str1 = 'ABCDEFGHIJKLIMNOQRSTUVWXYZ'
size = 4

def chunk(lst,n):
    for i in range(0,len(lst),n):
        yield lst[i:i+n]

k= list(chunk(str1,size))

for i in (k):
    print(i)

print("------------------")

out = [str1[i:i+size] for i in range(0,len(str1),size)]

(print(i) for i in out)



