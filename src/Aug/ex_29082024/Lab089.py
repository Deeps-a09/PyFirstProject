squares = [1, 4, 9, 16, 25]

# List is mutable in nature i.e. we can change value

squares[3] = 64
print(squares)


# Tuple- Collection of Items -> Are immutable, it has fixed data and List can have Dynamic Data
# List is mostly used

my_tuple = (1, 4, 9, 16, 25)
print(my_tuple)

# When we have to use list and when tuple

shopping_list_wife = ["bread", "butter", "paneer"]
shopping_list_wife[2] = "milk"
print(shopping_list_wife)

# Real world project
# Working with tw domains only- thetestingacademy.com and sdet.live

my_tuple = ("tta.com", "sdet.live")

#convert tuple to list

my_api_list = list(my_tuple)
print(my_api_list)

my_tuple = tuple(my_api_list)
print(my_tuple)
