def how_many_vowels(text, index=0, vowels_amount=None):
    if vowels_amount is None:
        vowels_amount = {}

    if index >= len(text):
        return vowels_amount

    elif text[index] in vowels:
        lowercase_vowel = text[index].lower()
        if text[index] in vowels_amount:
            vowels_amount[lowercase_vowel] += 1
        else:
            vowels_amount[lowercase_vowel] = 1

    return how_many_vowels(text, index+1, vowels_amount)


def recursive_crash(depth=0):
    print(f"Recursion depth: {depth}")
    recursive_crash(depth + 1)


vowels = "aeiouAEIOU"
test = "baadace"

result = how_many_vowels(test)
print(result)

recursive_crash()
