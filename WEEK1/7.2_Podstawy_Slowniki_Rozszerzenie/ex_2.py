dict = {'The Sensual World': 'Kate Bush', 'Shaday': 'Ofra Haza',
        'Achtung Baby': 'U2', 'Aion': 'Dead Can Dance', 'Invisible Touch': 'Genesis'}

while True:
    print("1. Show albums.")
    print("2. Check album.")
    print("3. Add new album.")
    print("4. Delete album.")
    mode = int(input("Choose what you want to do: "))
    print()

    match mode:
        case 1:
            print("Available albums:")
            for key in dict.keys():
                print(key)
            print()

        case 2:
            userInput = str(input("Enter album name: "))

            if userInput in dict.keys():
                print(f'Album {userInput} is performed by {dict.get(userInput)}.')
            else:
                print("No data.")
            print()

        case 3:
            newKeyDict = str(input("Enter a name for the new album: "))
            newValDict = str(input("Enter the artist of the given album: "))
            dict[newValDict] = newValDict
            print(dict)
            print()

        case 4:
            delKey = str(input("Enter the name of the album to be deleted: "))
            if delKey in dict.keys():
                dict.pop(delKey)
            else:
                print("The specified album does not exist.")
            print()