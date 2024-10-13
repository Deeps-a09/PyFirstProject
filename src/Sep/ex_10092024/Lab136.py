# Try & Catch in a Try & Catch with file upload if file is present in same package
import os

try:
    file = open("example.txt", 'r')
    print(file.read())
except FileNotFoundError as fnfe:
    print("File1 Not Found, fix the path or create a file")
finally:
    try:
        file.close()  # To close the file
    except NameError as ne:
        print(ne)

# File upload if file is present in different package

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

try:
    full_path = os.getcwd()
    print(full_path)
    file = open(full_path+"Dee.txt", 'r')
    print(file.read())
except FileNotFoundError as fnfe:
    print("File2 Not Found, fix the path or create a file")
finally:
    try:
        file.close()  # To close the file
    except NameError as ne:
        print(ne)