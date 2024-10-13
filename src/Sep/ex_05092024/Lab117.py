class Parent:
    gold = "2KG"  # Child can access all

    def BHK2(self):
        print("3BHK")


class Child(Parent):
    diamond = "2 kg"  # Parent can not access this diamond

    def BHK3(self):
        print("3BHK")


chil_object = Child()
print(chil_object.gold)
chil_object.BHK2()
chil_object.BHK3()
