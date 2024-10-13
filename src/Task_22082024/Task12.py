class Employee:
    name = None
    age = None
    phone = None
    address = None
    eid = None

    def __init__(self, name, age, phone, address, eid):
        self.name = name
        self.age = age
        self.phone = phone
        self.address = address
        self.eid = eid

    def walk(self):
        print("Employee " + self.name + " is walking")
        return None

    def talk(self):
        print("Employee " + self.name + " is talking")
        return None


emp1 = Employee(input("Enter name: "), int(input("Enter age: ")), int(input("Enter phone: ")), input("Enter address: "),
                input("Enter eid: "))
print("Employee details: \n", "Name: ", emp1.name, "Age: ", emp1.age, "Phone: ", emp1.phone, "Address: ", emp1.address,
      "EID: ", emp1.eid)
emp1.walk()
emp1.talk()

emp2 = Employee(input("Enter name: "), int(input("Enter age: ")), int(input("Enter phone: ")), input("Enter address: "),
                input("Enter eid: "))
print("Employee details: \n", "Name: ", emp1.name, "Age: ", emp1.age, "Phone: ", emp1.phone, "Address: ", emp1.address,
      "EID: ", emp1.eid)
emp2.walk()
emp2.talk()
