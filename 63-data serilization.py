import pickle

class Person():
    def __init__(self,name,age):
        self.name = name
        self.age = age


p1 = Person('Jack', 23)
pickle.dump(p1, open("pickle_test.txt", 'wb'))

p2 = pickle.load(open('pickle_test.txt', 'rb'))
print(p2.name,p2.age)