favColors = ['red', 'black', 'yellow']
userColors = str(input("Enter any number of colors separated by a space: "))
userColorList = userColors.split(" ")

if sorted(favColors) == sorted(userColorList):
    print("The colors listed are the same as your favorite colors.")
else:
    commonColors = [color for color in favColors if color in userColorList]
    print("Common colors:", end=" ")
    for color in commonColors:
        print(color,end=" ")
    print()

    onlyUserColors = [color for color in userColorList if color not in favColors]
    print('Preferred colors only by the user:', end=" ")
    for j in onlyUserColors:
        print(j, end=" ")
    print()

    onlyAuthorColors = [color for color in favColors if color not in userColorList]
    print('Preferred colors only by the author:', end=" ")
    for i in onlyAuthorColors:
        print(i, end=" ")
    print()