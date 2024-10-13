# OOPS -> Object Oriented Programming System, Something Related to Object -> CLass
# In OOPs we divide the program in class and objects
# Emphasis data.
# E.g. Python, Java
# Here productivity is high


# Procedural Programming Language -> Everything that we create a program, we can divide them into the functions.
# E.g. def sum(), sum (3,4)
# data members - Data variables and functions- methods -> PPL- most of things are focused on the functions only
# It is not that close to the real world
# Here the emphasis is on the doing things
# E.g. C, Basic
# Here productivity is very low

# Class and Object

class Person:
    # Attributes
    id = None
    name = None
    age = None
    email = None
    height = None
    gender = None
    Phone_no = None
    address =  None

    # Behaviour
    def talk(self):  # self is an argument, self will be the first argument in every behaviour
        print("I can talk")

    def sleep(self, name):
        print("I am a Method!!")
        print("Sleep", name)

    def sleep2(self, name):
        print("I am a Method!!")
        return None

    def walk(self):
        print("I am walking")

    def walk_return(self):
        return "I am walking"

tushar = Person()
tushar.name = "tushar"
print(tushar.name)
tushar.talk()

rajyalaxmi = Person()
tushar.name = "rajyalaxmi"
print(tushar.name)
rajyalaxmi.talk()
