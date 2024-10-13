# Encapsulation --> Bind Data Variables and methods, wrap them together
# Hide the data members, by using the methods- Private, Protected and Public


class Car:
    name = None
    #attributes
    password = 123

    def __inti__(self):
        print("DC")


def change_password(self):
    #methods
    self.password = "pramod"
#by this we can say methods can use attributes, we can hide data members and can be used by functions.

object_ref = Car()
print(object_ref.password)
print(object_ref.password)
