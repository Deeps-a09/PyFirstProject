class Person:
    # Class Variables
    # Instance Variables
    # name = "Amit" # When we assign the value in the class it becomes hard coded, therefore we use
    # constructor to change the value of instance variable during the object creation
    def __init__(self, name):
        self.name = name
    def walk(self):
        #self.name = name
        #print(self.name)
        return self.name

amit = Person("amit")
pramod = Person("pramod")
print(amit.name)
print(pramod.name)
print(amit.walk())

