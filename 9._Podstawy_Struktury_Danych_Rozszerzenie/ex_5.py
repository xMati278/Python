bill_items = [
    ['Tom', 'Calamari', 6.00],
    ['Tom', 'American Hot', 11.50],
    ['Tom', 'Chocolate Fudge Cake', 4.45],
    ['Clare', 'Bruschetta Originale', 5.35],
    ['Clare', 'Fiorentina', 10.65],
    ['Clare', 'Tiramisu', 4.90],
    ['Rich', 'Bruschetta Originale', 5.35],
    ['Rich', 'La Reine', 10.65],
    ['Rich', 'Honeycomb Cream Slice', 4.90],
    ['Rosie', 'Garlic Bread', 4.35],
    ['Rosie', 'Veneziana', 9.40],
    ['Rosie', 'Tiramisu', 4.90],
]

dishes = {}


for i in range(len(bill_items)):

    if bill_items[i][0] not in dishes:

        dishes[bill_items[i][0]] = {'dishes': [bill_items[i][1]], 'price': bill_items[i][2]}

    else:

        dishes[bill_items[i][0]]['dishes'].append(bill_items[i][1])
        dishes[bill_items[i][0]]['price'] = dishes.get(bill_items[i][0]).get('price') + bill_items[i][2]

for key, value in dishes.items():
    
    print(key, value)
