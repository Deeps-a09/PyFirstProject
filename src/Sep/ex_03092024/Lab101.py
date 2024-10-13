# Take user Input

class Person:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.age = input("Enter your age: ")
        self.phone = input("Enter your phone: ")
        self.occupation = input("Enter your occupation: ")

    def display_function(self):
        print(f"Name is {self.name}")
        print(f"Age is {self.age}")
        print(f"Phone is {self.phone}")
        print(f"Occupation is {self.occupation}")


# Create an Object
person1 = Person()

person1.display_function()
