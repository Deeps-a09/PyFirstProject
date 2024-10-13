# Multilevel Inheritance

class GrandFather:
    gold = "2kg"

    def bhk1(self):
        print("1BHK")


class Father(GrandFather):
    diamond = "22 karat"

    def bhk2(self):
        print("2BHK")


class Son(Father):
    btc = "1btc"

    def bhk3(self):
        print("3bhk")


son_obj = Son()
print(Son.gold)
print(Son.diamond)
print(Son.btc)
son_obj.bhk3()
son_obj.bhk2()
son_obj.bhk1()

father_obj = Father()
print(Father.gold)
print(Father.diamond)
# print(Father.btc) --> Not allowed because father can not access son's class
father_obj.bhk2()
father_obj.bhk1()
# father_obj.bhk3() --> Not allowed because father can not access son's class

gf_obj = GrandFather()
print(GrandFather.gold)
# print(GrandFather.diamond) --> Not allowed because grand father can not access father's and son's class
# print(GrandFather.btc) --> Not allowed because grand father can not access father's and son's class
gf_obj.bhk1()
# gf_obj.bhk2() --> Not allowed because grand father can not access father's and son's class
# gf_obj.bhk3() --> Not allowed because grand father can not access father's and son's class
