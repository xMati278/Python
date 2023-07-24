dict = {'The Sensual World' : 'Kate Bush', 'Shaday' : 'Ofra Haza', 'Achtung Baby' : 'U2', 'Aion' : 'Dead Can Dance', 'Invisible Touch' : 'Genesis'}

print("Available albums:")

for key in dict.keys():
    print(key)
print()

userInput = str(input("Enter album name: "))

if userInput in dict.keys():
    print(f'Album {userInput} is performed by {dict.get(userInput)}.')
else:
    print("No data.")