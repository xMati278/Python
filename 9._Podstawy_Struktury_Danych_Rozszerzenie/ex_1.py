commonItems = []

a = str(input("Enter the elements of the list A separated by a space:"))
b = str(input("Enter the elements of the list B separated by a space:"))

aItems = a.split(" ")
bItems = b.split(" ")


for i in range(len(aItems)):

    for j in range(len(bItems)):

        if aItems[i] == bItems[j]:
            commonItems.append(aItems[i])

if len(commonItems) == 0:
    print("There are no common elements")

else:

    print("Common elements: ", end = "")

    for k in range(len(commonItems)):

        if k < len(commonItems) - 1:
            print(commonItems[k],end = ", ")

        else:
            print(commonItems[k])