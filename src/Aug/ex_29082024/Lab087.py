my_list= [1,2,3]

#Append
my_list.append(4)  # We have added 4 in above list, at the end of the list
my_list.append(5)  # * args in append can only use the function multiple times, not multiple values
my_list.extend([6, 7, 8])# To use multiple elements in the list, we use Extend, where as append will always add
my_list.extend([10])
my_list.extend(["Dee"])
print(len(my_list))

my_list.insert(1, "Dutta") # To add element in btw, It will insert an element before index
print(my_list)
print(len(my_list))

my_list[1] = "Amit"
print(my_list)
print(len(my_list))

my_list.insert(0, 0)
print(my_list)
#my_list.insert(-1, "lucky")
#print(my_list)

my_list.remove("Amit")
print(my_list)

print("--------------------------------")
print("--------------------------------")


my_copy_list = my_list.copy()
print(my_list)
print(my_copy_list)

my_list.clear()
print(my_list)
print(my_copy_list)


#Sorting -- With string we cannt

my_copy_list.remove("Dee")   # Remove with index is not available
my_copy_list.sort()
#my_copy_list(reverse = False)
print(my_copy_list)

my_copy_list.reverse()  #Different from Desc
print(my_copy_list)



name = "Dee"
name = name.upper()
print(name)
