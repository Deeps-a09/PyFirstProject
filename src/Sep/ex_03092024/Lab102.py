# Create a Calculator
class Calculator:
    def __init__(self):
        print("Printing Calculator")

    def sum(self, a, b):
        return a + b

    def sub(self, a, b):
        return a - b

    def mul(self, a, b):
        return a * b

    def div(self, a, b):
        return a / b


calculation = Calculator()
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
result_sum = calculation.sum(a, b)
result_sub = calculation.sub(a, b)
result_mul = calculation.mul(a, b)
result_div = calculation.div(a, b)

print(f"Sum is: {result_sum}, Subtraction is: {result_sub}, Multiplication is: {result_mul}, Division is: {result_div}")

"""
class Calculator:

    def __init__(self, a, b):
        self.add = a + b
        self.sub = a - b
        self.mul = a * b
        self.div = a / b

    def display_function(self):
        print(f"Sum is: {self.add}")
        print(f"Sub is: {self.sub}")
        print(f"Mul is: {self.mul}")
        print(f"Div is: {self.div}")


obj = Calculator(5, 2)
obj.display_function()
"""
