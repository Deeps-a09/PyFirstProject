# Understanding Decorator
"""
Decorators are way to modify the behavious of a function or class without
changing source code
They are a powerful tool that allows you to wrap another function and
extend its functionality, while keeping the original function's code unchanged
"""


def my_decorator(func):
    # two parts- what we want to wrap and what we call
    def wrapper():
        print("1. Something before the function")
        print("2. helmet, safety guards")
        func()
        print("3. Something after the function is called.")
        print("4. Secure Driving")

    return wrapper()


@my_decorator
def drive_scooty():  # definition
    print("I am driving")

# drive_scooty()  #calling

# def drive_bike():
# print("normal function")
