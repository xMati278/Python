lovers = {1: 'Rahima', 2: 'Alishba', 3: 'Fizza'}
friends = {4: 'Bilal', 5: 'Arbab', 6: 'Shahzor'}

dictionary = lovers
dictionary.update(friends)

new_dictionary = lovers | friends

new_dictionary_1 = {**lovers, **friends}

print(dictionary)