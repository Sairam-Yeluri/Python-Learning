str = '$aiRam'

s = '''~!@#$%^&*()_+-=}{[]:";'<>?,./|'''
k = 0
for i in str:
    if s.find(i)>=0:
        k = 1

print("")
if k == 0:
    print("Good to go!!!")
else:
    print("Cant Accept:(")

print("")