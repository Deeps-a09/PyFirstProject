class VWOLoginPage:
    def __init__(self,email,pwd):
        self.email = email
        self.pwd = pwd

    def login_function(self):
        if self.email == "pramod@gmail.com" and self.pwd == "Pass123":
            print("Allowed to login")
        else:
            print("Not Allowed")

email = input("Enter Email: ")
pwd = input("Enter Pwd: ")

vwo_obj = VWOLoginPage(email,pwd)
vwo_obj.login_function()