removeChars = [',', '.', ':', ';', '!', '?']

text = str(input("Enter any sentence: "))

for char in removeChars:
    text = text.replace(char, '')

words = text.split(" ")

print(words[::-1])