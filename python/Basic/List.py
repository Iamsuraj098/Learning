arr = [1, 2, 3, 4]
print(arr)
print(type(arr))
arr2 = list()
print(type(arr2))
arr2.append(1)
arr2.append(2)
arr2.append(3)
arr2.append(4)
print(arr2)
print(arr2[0:3])


def hello(data):
    print(data)

# inset element 
arr2 = list()

arr2.append(1)
arr2.append(2)
arr2.append(3)
arr2.append(4)
arr2.append(5)
arr2.append(6)
arr2.append(7)
arr2.append(8)
arr2.append(9)
arr2.append(0)
arr2.append(11)

# get element
print("Hell: ", arr2[0], end=" ")
print("Hell: ", arr2[4], end=" ")
print("Hell: ", arr2[3], end=" ")
print("Hell: ", arr2[2], end=" ")

# iteration element
for i in range(len(arr2)):
    print("index", i, " ", arr2[i], end=' ')

for i in arr2:
    print("value: ", i, end=' ')

# slicing of the list
arr3 = arr2[0:5]
print("\nSliced List: ", arr3)

arr4 = arr2[0:10:3]
print("Sliced List with step: ", arr4)

arr5 = arr2[::-1]
arr2.remove(5)  # removes first occurrence of value 5
print(arr5)


# replace
arr2[9] = 111
print(arr2)

# sort
arr6 = [3, 1, 4, 2, 5]
arr6.sort()
print("Sorted List: ", arr6)
arr6.sort(reverse=True)
print("Sorted List in Descending order: ", arr6)