dict1 = {'name': 'Tom', 'age': 20, 'gender': 'male', 'id': 110}

print(dict1)

dict1['name'] = 'Rose'
print(dict1)

del dict1['name']
print(dict1)

print(dict1.get('name'))

print(dict1.keys())

print(dict1.values())

print(dict1.items())