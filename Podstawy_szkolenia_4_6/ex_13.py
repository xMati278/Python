
dictionary = {"Jan": "Kowalski"}

while True:
    print("1. Add new word with definition.")
    print("2. Find the definition of the word.")
    print("3. Remove the word along with the definition.")
    print("4. End the program.")

    mode = int(input("Choose what you want to do by entering the number."))

    match mode:
        case 1:
            new_key = input("Enter new key: ")
            new_value = input("Enter new value:")

            dictionary[new_key] = new_value

        case 2:
            findDef = input("Enter the word you are looking for a definition: ")
            print(f'The definition of the word {findDef} is: {dictionary.get(findDef)}')

        case 3:
            delKeyVal = input("Enter the word to be deleted: ")
            print(f'Key: {delKeyVal} with definition: {dictionary.get(delKeyVal)} has been deleted.')
            dictionary.pop(delKeyVal)

        case 4:
            break
    print("")