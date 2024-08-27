# def and call, if we are creating user defined function

def greet_to_all_of_you(): #Defining function 1
    print("Hello Everyone!")

def greet(): #Defining function 2
    print("Hello!")

greet() #Calling function no. 2
greet_to_all_of_you() #Calling function no. 1



#Can we call One function in another

def greet_to_all_of_you(): #Defining function 1
    print("Hello Everyone!")

def greet(): #Defining function 2
    print("Hello!")
    greet_to_all_of_you() #Calling function 1 inside function 1
greet() #But without calling function 2 we will not get our result