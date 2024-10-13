# Hierarchical Inheritance

# Eg. Father can have multiple sons

class Father:
    def BHK1(self):
        print("1BHK")


class Pramod(Father):
    def BHK2(self):
        print("2BHK")


class Amit(Father):
    def BHK3(self):
        print("3BHK")


class Lucky(Father):
    def no_house(self):
        print("No House")


pramod = Pramod()
pramod.BHK1()
pramod.BHK2()
# print(Pramod.BHK3())
amit = Amit()
amit.BHK1()
amit.BHK3()
# print(Amit.BHK2())
lucky = Lucky()
lucky.BHK1()
# print(Lucky.BHK2())
# print(Lucky.BHK3())
