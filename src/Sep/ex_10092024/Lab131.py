# Exceptions - > ANy event which disrupt the normal flow of a program when an error occurs
#  If we do not handle exception, python interpreter will ive its own exception which will decrease user experience


# 1. Arithmetic error
# print(10/0) ZeroDivisionError: division by zero

# print(1+ "1") #TypeError: unsupported operand type(s) for +: 'int' and 'str'

# print(int('a')) #ValueError: invalid literal for int() with base 10: 'a'

# my_list = [1, 2, 3]
# print(my_list[5]) #IndexError: list index out of range

# while True print("Hello wolrd") SyntaxError: invalid syntax

#    print("Hello worlds") IndentationError: unexpected indent
import os
try:
    file = open("C:\\Users\\spxlpt092.AzureAD\\PycharmProjects\\PyFirstProject\\src\\Sep\\ex_07092024\\Dee.txt", 'r')
    print(file.read())
except FileNotFoundError as fnfe:
    print("File2 Not Found, fix the path or create a file")
finally:
    try:
        file.close()  # To close the file
    except NameError as ne:
        print(ne)