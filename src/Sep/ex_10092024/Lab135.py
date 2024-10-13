# try, except and finally

try:
    num1 = int(input("Enter the num1:"))
    num2 = int(input("Enter the num2:"))
    result = num1 / num2

except ValueError as v:
    print("Value error, please enter number instead of string")
except ZeroDivisionError as z:
    print("Zero Division error, please enter number other than zero")
else:
    print(f"Result: {result}")
finally:
    print("This will always executed.!")