print("\nPython Program for simple interest")

principle = int(input("Enter Principle amount: "))
time = int(input("Enter time: "))
rate = float(input("Enter rate: "))

print("\nSimple Interest is",principle*time*rate/100)

print("------------------------------\n")



def simple_interest(p,t,r):
    print("Principle amount is: ",p)
    print("Time is: ",t)
    print("Rate is: ",r)
    print("Simple Interest is: ",p*t*r/100)

simple_interest(principle,time,rate)