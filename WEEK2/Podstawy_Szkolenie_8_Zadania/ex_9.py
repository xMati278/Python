import json
from pprint import pprint
from tabulate import tabulate


def read_json(data):
    data_info = []

    for row in data['imdata']:
        attributes = row['l1PhysIf']
        dn_info = attributes['dn']
        descr_info = attributes['descr']
        speed_info = attributes['speed']
        mtu_info = attributes['mtu']
        data_info.append({'dn_info': dn_info, 'descr_info': descr_info, 'speed_info': speed_info,
                          'mtu_info': mtu_info})
    return data_info
    # for key, value in file.items():
    #     if key == "totalCount":
    #         print(f'{key}: {value}')
    #     else:
    #         for x in value:
    #             for key1, value1 in x.items():
    #                 for value2 in value1.values():
    #                     for key3, value3 in value2.items():
    #                         if key3 == 'dn':
    #                             dn_info = value3
    #                         elif key3 == 'descr':
    #                             descr_info = value3
    #                         elif key3 == 'speed':
    #                             speed_info = value3
    #                         elif key3 == 'mtu':
    #                             mtu_info = value3
    #
    #                     data_info.append([dn_info, descr_info, speed_info, mtu_info])
    # print(tabulate(data_info, headers=headers, tablefmt="grid"))

headers = ['DN', 'Description', 'Speed', 'MTU']
with open('data.json') as json_file:
    data = json.load(json_file)
    read_json(data)
