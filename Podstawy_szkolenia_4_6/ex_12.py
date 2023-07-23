print("Aplhabet: ", end="")
for i in range(97, 123):
    if i < 122:
        print(f'{chr(i)}, ', end="")
    else:
        print(f'{chr(i)}', end="")
print()

print("Reverse alphabet: ", end="")

for j in range(90, 64, -1):
    if j > 65:
        print(f'{chr(j)}, ', end="")
    else:
        print(f'{chr(j)}', end="")
print()