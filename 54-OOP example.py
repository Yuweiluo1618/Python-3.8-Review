class A(object):
    def __init__(self):
        self.__num = 3

    def access(self):
        print(self.__num)


class B(A):
    pass

b = B()
b.access()
a = A()
a.access()