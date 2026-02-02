tup = (1, 2, 3, 4, 5)

# insertion
# tuple is immutable so cannot insert elements into it but we can overwrite it.
tup = tup + (6, 7, 8, 9)
print(tup)
# deletion
tup = tup[1:]  # Remove the first element (1)

# update
tup = tup[:3] + (111, ) + tup[4:]
print(tup)

lis = list(tup)
lis[2] = 222
tup = tuple(lis)
print(tup)

# iteration
for i in tup:
    print(i, end=' ')
print("\n ")

for i in range(len(tup)):
    print("index", i, " ", tup[i], end=' ')


# print
# print(tup)


# list to tuple converison
list2 = list(tup)
print(type(list2))

# unpack the tuple

tup2 = (1, 2, 3, 4)
a, b, c, d = tup2
print(type(a), b, c, d)

a, b, *c = tup2
print(a, b, type(c))


# multiplication in tuple
tup4 = ("apple", "mango")*2
print(tup4)
