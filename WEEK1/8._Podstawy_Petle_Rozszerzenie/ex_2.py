word = str(input("Enter a word: ")).lower()
wordCheck = word[::-1]

if word == wordCheck:
    print("This word is a palindrome.")
else:
    print("This word is not a palindrome.")