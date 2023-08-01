import random

setA = set()
setB = set()
setC = set()
setD = set()
setE = set()
setF = set()
randomAmount= 10

n = int(input("Enter a number: "))

# ##### SET A #####

for i in range(randomAmount):
    randomA = random.randint(0,n-1)

    if randomA % 2 != 0:
        randomA += 1

    setA.add(randomA)

print()
print("SET A")
print(f'Size: {len(setA)}')
print("Elements: ",end="")
if len(setA)>0:
    for aItem in sorted(setA):
        print(aItem, end=" ")
else:
    print("None")
print()

# ##### SET B #####

for j in range(randomAmount):
    randomB = random.randint(0,n-2)

    if randomB % 3 == 0:
        randomB += 2

    else:
        randomB += 1
    setB.add(randomB)
print()
print("SET B")
print(f'Size: {len(setB)}')
print("Elements: ",end="")
if len(setB)> 0:
    for bItem in sorted(setB):
        print(bItem, end=" ")
else:
    print("None")
print()

# ##### SET C #####

setC = setA.union(setB)

print()
print("SET C")
print(f'Size: {len(setC)}')
print("Elements: ",end="")
if len(setC)>0:
    for cItem in sorted(setC):
        print(cItem, end=" ")
else:
    print("None")
print()

# ##### SET D #####

setD = setA.intersection(setB)

print()
print("SET D")
print(f'Size: {len(setD)}')
print("Elements: ",end="")
if len(setD) > 0:
    for dItem in sorted(setD):
        print(dItem, end=" ")
else:
    print("None")
print()

# ##### SET E #####

setE = setA.difference(setB)

print()
print("SET E")
print(f'Size: {len(setE)}')
print("Elements: ",end="")
if len(setE) > 0:
    for eItem in sorted(setE):
        print(eItem, end=" ")
else:
    print("None")
print()

# ##### SET F #####

setF = setA.symmetric_difference(setB)

print()
print("SET F")
print(f'Size: {len(setF)}')
print("Elements: ",end="")
if len(setF) > 0:
    for fItem in sorted(setF):
        print(fItem, end=" ")
else:
    print("None")
print()

# ##### Check if set B is contained in set A #####

print()
if setB.issubset(setA):
    print('set B is contained in set A.')
else:
    print('set B is not contained in set A.')