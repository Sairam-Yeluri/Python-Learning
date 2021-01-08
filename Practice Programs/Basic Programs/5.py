print("\nPython Program for compound interest")

principle = int(input("Enter Principle amount: "))
nyears = int(input("Enter number of years: "))
rate = float(input("Enter rate: "))

k = principle*(1+(rate/100))**nyears
print("\nCompound interest is",k)

print("--------------------------\n")


def compound_interest(p,t,r):
    if p<=0 or t<=0 or r <= 0:
        return "Invalid Data"
    else:
        return p*(1+(r/100))**t

k =compound_interest(principle,nyears,rate)
print("Compound interest is",k)