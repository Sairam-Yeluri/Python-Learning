str = "SaiRamYeluri"
l = len(str)

#Right Rotate
Rn = 6
Rstr = str
Rs1 = Rstr[l-Rn:]
Rs2 = Rstr[:l-Rn]
Rs3 = Rs1+Rs2

print("\nRight Rotate is: ",Rs3)

Ln = 3
Lstr = str
Ls1 = Lstr[Ln:]
Ls2 = Lstr[:Ln]
Ls3 = Ls1+Ls2

print("\nLeft Rotate is: ",Ls3)
print("")