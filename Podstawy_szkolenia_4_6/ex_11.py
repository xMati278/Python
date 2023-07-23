print(" Shape 7x6 with filling")

for i in range(6):
    for j in range(7):
        print("*" ,end= " ")
    print()

print(" Shape 5x5 without filling")

for k in range(5):
    for l in range(5):
        if k == 0 or k == 4 or l == 0 or l == 4:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

print("Christmas tree with a base of 5")

for x in range(1, 6):
    print(" " * (5 - x) + "*" * (2 * x - 1))