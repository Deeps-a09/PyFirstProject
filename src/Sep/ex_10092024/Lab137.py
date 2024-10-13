import os

# operating system -- files, path related to the OS

print(os.name)  # nt
if os.name == 'posix':
    print("using mac")
else:
    print("window")

print(os.getcwd())
os.chdir("Downloads")  # change directory
print(os.getcwd())

os.mkdir('new_directory')  # new directory
os.makedirs('parent/cild/grandchild')  # folder inside folder
print(os.listdir('.'))  # list directory
for file in os.listdir('.'):
    print(file)

os.remove('example.txt')  # to remove file
os.rmdir()

os.rename('old_name.txt', 'new_name.txt')

full_path = os.path.join('', 'file.txt')
print(full_path)
print()
