text = 'Once upon a midnight dreary, while I pondered, weak and weary, Over many a quaint and curious volume of forgotten lore, While I nodded, nearly napping, suddenly there came a tapping, As of someone gently rapping, rapping at my chamber door. This visitor, I muttered, tapping at my chamber door - Only this, and nothing more.'
clearText = text.replace(",", "").replace(".", "")
clearLowerText = clearText.lower()
wordList = clearLowerText.split(" ")
words = set(wordList)

dictWord = {}
for i in words:
    dictWord[i] = wordList.count(i)

print(dictWord)