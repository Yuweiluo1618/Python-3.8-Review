class Dog(object):
    def work(self):
        pass

class AttackDog(Dog):
    def work(self):
        print("ad Dog")

class DrugDog(Dog):
    def work(self):
        print("dd Dog")

class Person(object):
    def work_with_dog(self, type):
        type.work()


police = Person()
ad = AttackDog()
dd = DrugDog()

police.work_with_dog(ad)
police.work_with_dog(dd)