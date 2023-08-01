import json


def reverse_json_dict(**kwargs):
    reverse_dictionary = {}
    for key, element in kwargs.items():
        for i in range(len(kwargs)):
            reverse_dictionary[element] = key
    print(reverse_dictionary)

    with open("output.json", "w") as json_output:
        json.dump(reverse_dictionary, json_output)


reverse_json_dict(name="John", age=30, color_eye="blue")
