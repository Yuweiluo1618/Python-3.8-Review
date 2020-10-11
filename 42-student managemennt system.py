def info_print():
    print('Select Function-------------')
    print('1.add')
    print('2.delete')
    print('3.update')
    print('4.query')
    print('5.show all')
    print('6.quit')


info = []


def add_Info():
    new_name = input('name: ')
    new_id = input('id: ')
    new_cell = input('cell: ')

    global info

    for i in info:
        if new_name == i['name']:
            return

    dict1 = {}
    dict1['name'] = new_name
    dict1['id'] = new_id
    dict1['cell'] = new_cell
    info.append(dict1)


def del_Info():
    del_name = input('name want to delete')
    global info
    for i in info:
        if i['name'] == del_name:
            info.remove(i)
            break
    else:
        print('no this name')

def modify_info():
    modify_name = input('name you want to modify')
    global info
    for i in info:
        if i['name'] == modify_name:
            i['cell'] = input('new cell')
            break
    else:
        print('name not exist')

def search_info():
    search_name = input('name want to search')
    global info
    for i in info:
        if i['name'] == search_name:
            print(i['name'])
            break
    else:
        print('name not exist')

def print_all():
    global info
    for i in info:
        print(f"{i['name']}")

while True:
    # 1. 显示功能界面
    info_print()

    # 2.用户输入功能序号
    user_num = int(input('select one function:'))

    # 3.按照用户输入执行不同的功能
    if user_num == 1:
        add_Info()

    elif user_num == 2:
        del_Info()

    elif user_num == 3:
        modify_info()

    elif user_num == 4:
        search_info()

    elif user_num == 5:
        print_all()
    else:
       break
