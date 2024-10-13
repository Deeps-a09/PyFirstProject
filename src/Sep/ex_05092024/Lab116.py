# Inheritance

class Father:
    key = "2BHk"

    def car(self):
        print("Father car!!", "ALTO")
        print("Father car!!", "ALTO", self.key)


class Son(Father):
    key2 = "3BHK"

    def home(self):
        print("3BHK")

    def truck(self):
        print("Aura")

    pass


father_obj = Father()
father_obj.car()

son_obj = Son()
son_obj.truck()
