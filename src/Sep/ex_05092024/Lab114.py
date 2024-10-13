class Bank:
    def __init__(self, account_num, balance):
        self.balance = balance
        self.__account_num = account_num

    def deposit(self, amount):
        self.balance = self.balance + amount

    def check_balance(self):
        print(self.balance)

    def show_me_account_num(self, is_auth):
        if is_auth == True:
            print(self.__account_num)
        else:
            print("Not Allowed")


# def __interal_method(self):
#     print("PM")
#    print(self.__account_num)
#   self.show_me_account_num()


icici = Bank(2818918921, 100)
icici.deposit(100)
icici.check_balance()
# print(icici.check_balance())
print(icici.show_me_account_num(False))
