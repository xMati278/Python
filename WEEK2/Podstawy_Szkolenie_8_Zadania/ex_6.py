test_file = open("ex_6_test.txt", 'r')
file_lines = test_file.readlines()

for i in range(len(file_lines)):
    if i == 3:
        print(file_lines[i])

test_file.close()