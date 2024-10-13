# Nested Function
def outer(a, b):
    def inner(x, y):
        return x + y

    result = inner(a, b)
    return result


num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
result = outer(num1, num2)
print(f"Sum= {result}")
