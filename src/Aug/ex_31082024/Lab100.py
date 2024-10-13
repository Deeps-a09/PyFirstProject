# Constructor -> To set the value automatically, it is a special function
# __init__(), it will be automatically called when we create an object

class Dog:
    name = None
    age = None

    def __init__(self, name, age):
        #print("Called, Object is called")
        self.name = name
        self.age = age
    def sleep(self):
        #print("Sleeping")
        print("Who is Sleeping" + self.name, self.age)
        return None

dog1 = Dog("chow",10)
print(dog1.name)
dog1.sleep()

dog2 = Dog("mow", 20)
print(dog2.name)
dog2.sleep()