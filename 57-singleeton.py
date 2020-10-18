class Singleton(object):
    __instance = None
    __isFirst = True

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance

    def __init__(self, a, b):
        if self.__isFirst:
            self.a = a
            self.b = b
            self.__isFirst = False
        return


p1 = Singleton('1', '1')
p2 = Singleton('2', '2')

print(p1.a)
print(p2.a)
