
dict = {"Jan":"Kowalski"}

while 1:
    print("1. Add new word with definition.")
    print("2. Find the definition of the word.")
    print("3. Remove the word along with the definition.")
    print("4. End the program.")

    mode = int(input("Choose what you want to do by entering the number."))

    match mode:

        case 1:
            newKey = input("Enter new key: ")
            newValue = input("Enter new value:")

            dict[newKey]= newValue

        case 2:
            findDef = input("Enter the word you are looking for a definition: ")
            print(f'The definition of the word {findDef} is: {dict.get(findDef)}')

        case 3:
            delKeyVal = input("Enter the word to be deleted: ")
            print(f'Key: {delKeyVal} with definition: {dict.get(delKeyVal)} has been deleted.')
            dict.pop(delKeyVal)

        case 4:
            break
    print("")