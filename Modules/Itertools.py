from itertools import *

prod = product([1, 2], [3, 4])
print(list(prod))
# Cartesian Product: [(1, 3), (1, 4), (2, 3), (2, 4)]
prod = product([1, 2], [3], repeat=2)
print(list(prod))
# Cartesian Product repeating twice

print("------------------------")

perm = permutations([1, 2, 3])
print(list(perm))
#All Possible permutations

# optional: the length of the permutation tuples
perm = permutations([1, 2, 3], 2)
print(list(perm))

print("------------------------")

# the second argument is mandatory and specifies the length of the output tuples.
comb = combinations([1, 2, 3, 4], 2)
print(list(comb))

comb = combinations_with_replacement([1, 2, 3, 4], 2)
print(list(comb))
#Allows Repeted Values(1,1)

print("------------------------")

# return accumulated sums
acc = accumulate([1,2,3,4])
print(list(acc))
#[1,2,6,10]

print("------------------------")

def smaller_than_3(x):
    return x < 3
l = [1, 2, 3, 4]
groupobj = groupby(l, key=smaller_than_3)
#print(list(groupobj))
for key, group in groupobj:
    print(key, list(group))