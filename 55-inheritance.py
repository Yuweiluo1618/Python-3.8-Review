class Father1(object):
    def __init__(self):
        self.num = 1

    def info(self):
        print(self.num)


class Father2(object):
    def __init__(self):
        self.num = 2

    def info(self):
        print(self.num)


class Son(Father1, Father2):

    def __init__(self):
        self.num = 3

    def info(self):
        self.__init__()
        print(self.num)

    def call_father1(self):
        Father1.__init__(self)
        Father1.info(self)

    def call_father2(self):
        Father2.__init__(self)
        Father2.info(self)

    def call_both(self):
        super().__init__()
        super().info()


class Tusun(Son):
    pass


sunzi = Tusun()
sunzi.call_both()
#sunzi.info()
#sunzi.call_father1()
#sunzi.call_father2()
