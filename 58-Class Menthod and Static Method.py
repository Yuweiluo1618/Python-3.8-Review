class Person(object):
    height = 10
    @classmethod
    def cms(cls):
        print(cls.height)


    @staticmethod
    def sms():
        print('hello world')


p1 = Person()
p1.cms()
Person.cms()

p1.sms()
Person.sms()