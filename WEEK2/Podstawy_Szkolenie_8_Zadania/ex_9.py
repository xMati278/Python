import json
from tabulate import tabulate


def read_json(file):
    data_info = []
    headers = ['DN', 'Description', 'Speed', 'MTU']
    dn_info = None
    descr_info = None
    speed_info = None
    mtu_info = None

    for key, value in file.items():
        if key == "totalCount":
            print(f'{key}: {value}')
        else:
            for x in value:
                for key1, value1 in x.items():
                    for value2 in value1.values():
                        for key3, value3 in value2.items():
                            if key3 == 'dn':
                                dn_info = value3
                            elif key3 == 'descr':
                                descr_info = value3
                            elif key3 == 'speed':
                                speed_info = value3
                            elif key3 == 'mtu':
                                mtu_info = value3

                        data_info.append([dn_info, descr_info, speed_info, mtu_info])
    print(tabulate(data_info, headers=headers, tablefmt="grid"))


with open('data.json') as json_file:
    data = json.load(json_file)
    read_json(data)
