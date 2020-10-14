def valid_name(name):
    while name[0] == '.':
        print('invalid file name')
        name = input('file you want to back up')

    return name



file_name = input('file you want to back up')
old_name = valid_name(file_name)

index = old_name.rfind('.')
new_name =old_name[:index]+'[back up]'+old_name[index:len(old_name)]

f_old = open(old_name, 'rb')
f_new = open(new_name, 'wb')

while True:
    con = f_old.read(1024)
    if len(con) == 0:
        break
    f_new.write(con)

f_old.close()
f_new.close()

