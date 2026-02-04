# dictonary
my_dict = {
    "name": "Raja",
    "age" : 23,
    "address": "A-207, Astric, South-Moon,33003"
}

print(my_dict)

print(my_dict["address"])

# update value
my_dict["age"] = 25
my_dict.update({"name": "Raja Moon"})

# add value
my_dict["phone"] = "ABC-001"
my_dict.update({"email": "raja001&xail.moon"})

print(my_dict)

# change key name
my_dict["full_name"] = my_dict.pop("name")

# iteration 
for key in my_dict:
    print("key: ", key, "value: ", my_dict[key])

# iteration using the keys
for key in my_dict.keys():
    print("key: ", key)

# iteration using the values:
for value in my_dict.values():
    print("value: ", value)

# interation using items
for key, value in my_dict.items():
    print("key: ", key, " value: ", value)

# Copy dictonary
new_dict = my_dict.copy()
print("Copied Dictionary: ", new_dict)

my_dict2 = dict(my_dict)
print("Copied Dictionary 2: ", my_dict2)

# pop/delete items
my_dict.pop("age")
print(my_dict)

my_dict.popitem()  # removes last inserted item
print(my_dict)

del my_dict["address"]
print(my_dict)



# nested dictonary
child1 = {
    "name": "Child One",
    "age": 5
}

child2 = {
    "name": "Child Two",
    "age": 3
}

child3 = {
    "name": "Child Three",
    "age": 1
}

parents = {
    "parent_name": "Parent One",
    "children": {
        "child1": child1,
        "child2": child2,
        "child3": child3
    }
}

print("Parent Dictionary: ", parents)

# access nested dictonary
print("Child2 Name: ", parents["children"]["child2"]["name"])

# loop
for child_key, child_value in parents["children"].items():
    print("Key: ", child_key, " Value: ", child_value)