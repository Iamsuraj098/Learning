# loops

x = [1, 2, 3, 4, 5]

for i in x:
    print(i, end=" ")

print()
for i in "Kite":
    print(i, end=" ")


# breaks
print()
for i in x:
    if i==4:
        break
    print(i, end=" ")

# continues
print()
for i in x:
    if i==4:
        continue
    print(i, end=" ")


# range
print()
for i in range(2):
    print(i, end=" ")

print()
for i in range(2, 6):
    print(i, end=" ")

print()
# function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
for i in range(2, 11, 2):
    print(i, end=" ")


# Else in for loop
print()
for i in range(3):
    print(i, end=" ")
else:
    print("Done")


print()
for i in range(3):
    if i==2:
        break
    print(i, end=" ")
else:
    print("Done")


# Nested Loops:
print()
for i in range(3):
    for j in range(2):
        print(i, j, end=" | ")