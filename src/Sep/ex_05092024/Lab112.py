class MyCLass:
    # Public Instance variable
    public_var = "I am PUBLIC"
    balance = "0"

    # Private -- We Can not access the private variables outside the class
    __private_var = "I am Private"
    __password = "123"

    # Protected -- We can access the protected variables within the same package
    _protected_var = "I am Protected"


object = MyCLass()
print(object.public_var)  # Object can access public variable
print(object.balance)  # Object can access public variable
print(object._protected_var)  # Object can access public variable
# print(object.__private_var) #Object can not access private variable
# print(object.__password) #Object can not access private variable
