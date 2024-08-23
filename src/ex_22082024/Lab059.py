user_type= input("Enter the user type")
match user_type:
    case "admin" | "Manager":
        print("Hello Sir")
    case "guest":
        print("guest")
    case _:
        print("Hello")