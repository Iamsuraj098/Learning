# Stack
# It is a linear data structure
# Follows LIFO (Last In First out) principle
# Basic operations:
# push
# pop
# peek
# isEmpty 
# size

top = 0
global size
size = -1
capacity = 5
x = [1, 2, 3]

# isEmpty
def isEmpty():
    if size < capacity:
        print("Stack undeflow")
        return True
    else:
        return False

# is full
def isFull():
    if size >= capacity:
        print("Stack overflow")
        return True
    else:
        return False
# push operation

def push(element):
    n = len(x)
    if not isFull():
        size += 1
        return x.append(n)

# pop  element
def pop():
    if not isEmpty():
        size -= 1
        return x.pop()
    
# get top element
def top():
    if not isEmpty():
        return x[len(x)-1]

print(isFull())
print(isEmpty())

print(push(1))
print(push(1))
print(push(1))
print(push(1))
print(push(1))
