class Washer():
    def print_info(self):
        print(self.height)
        print(self.weight)

haier = Washer()
haier.height = 10
haier.weight = 20
haier.print_info()