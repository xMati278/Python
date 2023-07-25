removeChar = [',' '.' ':' ';' ',' '!' '?']
upperWords = []
findWords = ['i', 'w', 'na', 'pod', 'dla']

sentence = str(input("Enter a sentence:"))
print()

sentenceWords = sentence.split(" ")

print(f'Number of words in a sentence: {len(sentenceWords)}')
print()

for word in sentenceWords:
    if word and word[0].isupper():
        upperWords.append(word)

if len(upperWords) == 0:
    print("The sentence does not have words that start with a capital letter.")
else:
    print(f'Words starting with a uppercase letter: {upperWords}')
print()


for x in findWords:
    print(f'Words with the word {x} :', end = " ")
    amount = 0

    for i in range(len(sentenceWords)):
        if sentenceWords[i] == x:
            print(f'[{i}]', end = " ")
            amount += 1

    if amount == 0:
        print('None')
    else:
        print()

print()
sentenceWords.sort()
print(f'Sorted words: ', end ="")
for word in sentenceWords:
    print(word, end=" ")