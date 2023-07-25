n = int(input("Number of fibonacci numbers: "))

fibNumbers = []

for i in range(n+1):
    if i == 0:
        fibNumbers.append(0)
    elif i == 1:
        fibNumbers.append(1)
    else:
        fibNumbers.append(fibNumbers[i-2] + fibNumbers[i-1])

for j in range(len(fibNumbers)):
    if j < len(fibNumbers) - 1:
        print(fibNumbers[j], end=", ")
    else:
        print(fibNumbers[j], end="")