# Understanding Decorator
"""
Decorators are way to modify the behavious of a function or class without
changing source code
They are a powerful tool that allows you to wrap another function and
extend its functionality, while keeping the original function's code unchanged
"""


def add_bfore_ui_after_ui(custom_func_for_adding_extra_security):
    # two parts- what we want to wrap and what we call
    def wrapper():
        print("1. before running UI UC")
        print("2. Start the browser")
        custom_func_for_adding_extra_security()
        print("3. Ending the running UI UC")
        print("4. Quit the browser")

    return wrapper()


@add_bfore_ui_after_ui
def test_ui():
    print("I will test UI")

# @my_decorator
# def drive_scooty(): #definition
#   print("I am driving")

# drive_scooty()  #calling

# def drive_bike():
# print("normal function")
