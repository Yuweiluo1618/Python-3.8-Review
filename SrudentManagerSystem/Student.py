class Student(object):
    def __init__(self, name, gender, cell):
        self.name = name
        self.gender = gender
        self.cell = cell

    def __str__(self):
        return f"name: {self.name} gender: {self.gender} cell: {self.cell}"


if __name__ =='__main__':
    st1 = Student("Jack", 'male', 110)
    print(st1.__dict__)