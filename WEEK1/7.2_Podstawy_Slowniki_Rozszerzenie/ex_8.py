dict = { "V":"S001", "VI": "S002", "VII": "S001", "VIII": "S005", "IX":"S005", "X":"S009", "XI":"S007" }

for i in dict.values():
    if list(dict.values()).count(i) == 1:
        print(i)