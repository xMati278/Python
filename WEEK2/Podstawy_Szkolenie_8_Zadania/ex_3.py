poem_file = open('ex_3_przyklad.txt', 'r', encoding='utf-8')
poem_lines = poem_file.readlines()

for i in range(len(poem_lines)):
    if i % 2 == 1:
        print(poem_lines[i])

poem_file.close()
