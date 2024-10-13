# List- Collection of items(Duplicates are allowed), we can have same and different both type of data
# Index starts from 0 and len always starts from 1


my_list = [1, 2, 3] #Same type
#my_list2 =[1, True, "Pramod", 12.34] #Different type data

print(my_list)
print(len(my_list))
print(my_list[0])


my_list[0]= "Pramod"
my_list[1]= "Dee"
my_list[2]= "Dee2"
# my_list[10]= "Dee2" Not aalowed

#Indexing

print("element at the index 0", my_list[0])
print("element at the index 0", my_list[2])
print("element at the index 0", my_list[1])

print(my_list)

for element in my_list:
    print(element)

    #range(1,10,1) , its provide length -> []1,2,3,4,5,6,7,8,9

for i in range(1,10):
    print(i)

#if already have list we didn't use range

# Reassign
print("_ ______")
my_list= [1,2,3]

#Append
my_list.append(4)  # We have added 4 in above list, at the end of the list
my_list.append(5)  # * args in append can only use the function multiple times, not multiple values
my_list.extend(6, 7, 8)  # * args in append can only use the function multiple times, not multiple values
print(my_list)
