text_file = open('ex_7_przyklad.txt', 'r', encoding='utf-8')
new_text_file = open('ex_7_przyklad_new.txt', 'w', encoding='utf-8')
text_lines = text_file.readlines()

to_remove = []

for i in range(len(text_lines)):
    line = text_lines[i].split(" ")
    new_line = line.copy()
    for j in range(1, len(line)):

        if line[j].rstrip('\n') == line[j-1] or line[j] == line[j-1]:
            new_line.pop(j-1)

    new_line = " ".join(new_line)
    new_text_file.write(new_line)


new_text_file.close()
text_file.close()