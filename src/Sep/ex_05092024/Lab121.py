# Hybrid Inheritance

# Mixture of two or more type of Inheritance

class Father():
    def bhk1(self):
        print("Head of the Family")


class Mother(Father):
    def gold(self):
        print("Head Lady of the Family")


class Son(Mother):
    def bhk2(self):
        print("Son of the Family")


class Daughter(Mother, Father, Son):
    def nothing_personal(self):
        print("Daughter of the Family")

daughter = Daughter()
daughter.bhk1()
daughter.gold()


son = Son()
son.gold()
son.bhk2()

