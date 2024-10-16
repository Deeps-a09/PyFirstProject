# Custom exception--> User defined exception
import os


class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)

    balance = 100
    withdraw = int(input("Enter the amount you want to withdraw: "))
    if withdraw > balance:
        raise MyCustomException("Balance is low!")
    else:
        print("Remaining Balance", (balance - withdraw))
