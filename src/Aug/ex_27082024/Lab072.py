# Funation Scope


global_b = 12  # almost work like gloval variable, if it is in top


def my_function():
    a = 10  # local variable
    print(a)
    print(global_b)


def f1():
    print(global_b)


my_function()
print(global_b)
f1()
