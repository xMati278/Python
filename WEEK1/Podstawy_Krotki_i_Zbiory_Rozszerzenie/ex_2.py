sentence = str(input("Enter a sentence: "))
charToRemove = " ,.:;!?"

for char in charToRemove:
    sentence = sentence.replace(char," ")

words = sentence.split()
tupleSentence = tuple(words)

print(f'Total number of words(tuple): {len(tupleSentence)}')

print("All words in one line(tuple): ", end='')
for word in tupleSentence:
    print(word, end=" ")
print()

print(f'First word in tuple(tuple): {tupleSentence[0]}')
print(f'Fourth word in tuple(tuple): {tupleSentence[3]}')

setSentence = set(words)
print(f'Number of unique words (set): {len(setSentence)}')

print("All words in one line(set): ", end="")
for x in setSentence:
    print(x, end=" ")
print()

setSentenceList = list(setSentence)
print(f'First word in set(set): {setSentenceList[0]}')
print(f'Fourth word in set(set): {setSentenceList[3]}')

if tupleSentence[0] == setSentenceList[0]:
    print("The first element of the set and the tuple are the same.")
else:
    print("The first element of the set and the tuple are not the same.")

if tupleSentence[3] == setSentenceList[3]:
    print("The fourth element of the set and the tuple are the same.")
else:
    print("The fourth element of the set and the tuple are not the same.")