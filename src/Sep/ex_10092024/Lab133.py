# How to handle exception--> Try and Except

print("Start of the Program")
try:
    a = int(input("Enter num1: "))
    b = int(input("Enter num2: "))
    c = a / b
    print("Result div is: ", c)
except Exception as e:
    print(e)
    print("Please check your inputs, it shouldn't be string or zero")
print("End of the Program")
