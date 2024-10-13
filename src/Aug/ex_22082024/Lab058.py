# match keyword -> It is basically switch in Java

# Q- Write program to ask the user,Which Browser he want to run automation


browser_name = input("ENter Browser name: ")
browser_name = browser_name.lower() #aalow user cap and smal letters
match browser_name:
    case "firefox":
        print("Execute the firfox code")
    case "chrome":
        print("Execute the chrome code")
