# identity operator
# Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location

x = ["apple", "banana", "cherry"]
y = x

print(x is y)  # returns True because x and y point to the same object
print(x is not y)  # returns False because x and y point to the same object

y = ["apple", "banana", "cherry"]
print(x is y)  # returns False because x and y do not point to the same object, even if they have the same content
print(x is not y)  # returns True because x and y do not point to the same object

a = 5
b = 5
print(a is b)  # returns True because a and b point to the same object


# Difference between 'is' and '=='
# is -> check if both varaiables point to same object
# == -> check if both varaiables have same value

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # True because they have same value
print(x is y)  # False because they are different objects in memory
