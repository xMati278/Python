def count_nested_levels(data, level=1):
    max_level = level
    if isinstance(data, (dict, list, tuple, set)):
        for item in data:
            nested_level = count_nested_levels(item, level + 1)
            max_level = max(max_level, nested_level)
    return max_level


my_data = [
    {
        'a': 1,
        'b': {
            'c': [2, 3],
            'd': (4, 5)
        }
    },
    [
        {'e': 6},
        {'f': {7, 8}},
        ('g', {'h': 9})
    ],
    ('i', [10, 11])
]

nested_levels = count_nested_levels(my_data)
print("Number of nesting levels:", nested_levels)
