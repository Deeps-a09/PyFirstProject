# Method Overriding -> Same name in the parent and child
# Child always override the parent functions(because local has the preference)
# super means call my parent function
class GrandFather:
    x = 12
    def home(self):
        print("Old Home")
class Father(GrandFather):
    a = 10
    def home(self):
        print("1 bhk")
        print(self.a)
        print(super().x)

class Son(Father):
    b = 5
    def home(self):
        super().home() #super keyword, used to call parent function
        print(super().a)
        print("No House")
        print(self.b)

pramod = Son()
pramod.home()
# Line 11 will get call, local will be preferred. Though we can call Father's "home" function as well, by using "super()"
# keyword