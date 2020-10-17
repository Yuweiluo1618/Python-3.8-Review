#init
class Washer1():
    def __init__(self):
        self.height = 500
        self.weight = 600

    def __str__(self):
        return "this is object for Washer"

    def __del__(self):
        print("object has been deleted")


haier = Washer1()
print(haier.height)
print(haier.weight)
print(haier)