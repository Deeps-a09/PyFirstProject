#DIctionary

student_info = {
    "name": "Pramod",
    #"age": 78,
    "age": 79,
    "Address" : "KA"

}

print(student_info)
print(student_info["name"])
print(student_info["age"])
print(student_info["Address"])


student_info["age"] = 100
print(student_info)


#student_info = dict( name="Pramod", age= 79, Address=  "KA")
#print(student_info)

# A Dict is unordered

#Multiple DIct


student_info = {
    "name": "Pramod",
    #"age": 78,
    "age": 79,
    "Address" : {
        "home_add": "KA",
        "Off_add": "NA"
    }
}
print(student_info)


