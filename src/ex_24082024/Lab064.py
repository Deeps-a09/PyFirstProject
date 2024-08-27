# user Defined function-
#1. They can not return anything, No return type and no parameter(NR NP)

def greet_by_name():
    print("Hello")

result = greet_by_name()
print(result)

#2. No return type with argumet

def greet_by_name(name):
    print("Hello", name)
greet_by_name("Dee")

#3. No Return type with default argument

def say_hello_to(name="Dee"):
    print("Hello",name)

say_hello_to("Fen")
say_hello_to()
say_hello_to(name= "Promod") #Positional Argument




#multiple args
def multple_args(name1, name2, name3):
    print("multple_args", name1,name2,name3)

multple_args(name = "Dee")



#4. Argument and return type

def sum_of_two_num(num1,num2):
    return num1+num2

def sum_of_two_num_default(num1=20,num2=34):
    return num1+num2
result = sum_of_two_num_default()
print(result)


