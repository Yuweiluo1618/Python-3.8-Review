dict1 = {i: i ** 2 for i in range(1, 5)}
print(dict1)

list1 = ['name', 'age', 'gender', 'id']
list2 = ['tom', 22, 'male']

dict2 = {list1[i]: list2[i] for i in range(min(len(list1), len(list2)))}
print(dict2)

dict3 = {'mcpr': 300, 'asus': 100, 'huawei': 200}
dict4 = { key: value for key, value in dict3.items() if value >= 200}
print(dict4)
