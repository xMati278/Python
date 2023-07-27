dict = {'a' : 3, 'b' : 1, 'c' : 10, 'd' : 15, 'e' : 20}
reverseDict = {}

for key, value in dict.items():
    reverseDict[value] = key

print(reverseDict)