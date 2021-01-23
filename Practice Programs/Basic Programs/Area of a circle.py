PI = 22/7
r = float(input("Enter radius of circle: "))
area = PI * r**2

print("area of circle with radius",r,"is",area)

print("----------------------------------\n")

def circlearea(r):
    pi = 22/7
    area = pi * r**2
    return area

a = circlearea(r)
print("area of circle with radius",r,"is",a)

