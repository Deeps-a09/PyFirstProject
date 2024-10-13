# Global Variable and Instance Variable

a = 10  # Globally Defined

class Person:
    b = 11  # Instance Variable

    def print_info(self):
        global a
        a = "Hello"  # Modified a "Global varibale"
        print(a)
        print(self.b)


object_Ref = Person()
object_Ref.print_info()
print(a)
