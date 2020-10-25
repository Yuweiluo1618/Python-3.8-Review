from Student import *


class ManagerSystem(object):
    def __init__(self):
        self.student_list = []

    def load_data(self):
        try:
            f = open('student.data', 'r')
        except:
            f = open('student.data', 'w')
        else:
            content = f.read()
            new_list = eval(content)
            self.student_list = [Student(i['name'], i['gender'],i['cell']) for i in new_list]
        finally:
            f.close()
        print(self.student_list)

    @staticmethod
    def show_menu():
        print('Please select the service below:')
        print('1. add student')
        print('2. delete student')
        print('3. update student')
        print('4 query student')
        print('5 query all student')
        print('6 save all changes')
        print('7 quit system')

    def add_list(self):
        student_name = input('enter student name:')
        student_gender = input('enter student age:')
        student_cell = int(input('enter student cell:'))
        student = Student(student_name, student_gender, student_cell)
        self.student_list.append(student)
        print(self.student_list[0])

    def remove_list(self):
        student_name = input('enter the name you want to delete: ')
        for i in self.student_list:
            if i.name == student_name:
                self.student_list.remove(i)
                break
        else:
            print("No this Student")
        print(self.student_list)

    def change_list(self):
        student_name = input('enter the name you want to update: ')
        for i in self.student_list:
            if i.name == student_name:
                student_gender = input('the gender you want to update: ')
                student_cell = input('the cellphone you want to update:')
                i.gender = student_gender
                i.cell = student_cell
                break
        else:
            print('no this student')
        print(self.student_list[0])

    def get_list(self):
        student_name = input('enter the name you want to query: ')
        """
        for i in self.student_list:
            if i.name == student_name:
                print(f'name: {i.name} gender: {i.gender} cell: {i.cell}')
                break
        else:
            print('no this student')
        """
        result = filter(lambda student: student.name == student_name, self.student_list)
        if len(list(result)) == 0:
            print('no this student')
            return
        for x in result:
            print(x)

    def get_all(self):
        for i in self.student_list:
            print(i)

    def save_list(self):
        f = open('student.data', 'w')
        new_list = [i.__dict__ for i in self.student_list]
        f.write(str(new_list))
        f.close()

    def run(self):

        self.load_data()

        while True:
            self.show_menu()
            menu_num = int(input("please select one service: "))

            if menu_num == 1:
                self.add_list()

            elif menu_num == 2:
                self.remove_list()

            elif menu_num == 3:
                self.change_list()

            elif menu_num == 4:
                self.get_list()

            elif menu_num == 5:
                self.get_all()

            elif menu_num == 6:
                self.save_list()

            elif menu_num == 7:
                break
