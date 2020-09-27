import random
teachers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
offices = [[], [], []]

for name in teachers:
    num = random.randint(0, 2)
    offices[num].append(name)

i = 1
for office in offices:
    print(f'office{i} people : {len(office)}')
    for name in office:
        print(f'{name}')

    i += 1

