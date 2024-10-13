# Pass Function as argument

def add(x, y):
    return x + y


def operate(func, a, b):
    return func(a, b)


num1 = int(input("Enter num 1: "))
num2 = int(input("Enter num 2: "))
result = operate(add, num1, num2)
print(result)
