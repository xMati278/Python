def printStrings(data):

    if isinstance(data, dict):
        for key, value in data.items():
            printStrings(value)

    elif isinstance(data, list):
        for element in data:
            printStrings(element)

    elif isinstance(data, str):
        print(data)


dane = {
    'data':
        [1, 2, 'asd', [2, 3, 4, 5]],
    'nested_analysis': {
        'analysis_1':
            [1, 10, 15, 120.2, '120'],
        'analysis_2':
            [10, 100, 'test', 200, 300],
    },
    'probes':
        [['probe_1', 'probe_2'], 'probe_3']
}

printStrings(dane)