class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def singLinkedList(data):
    return Node(data)

head = None

# Element insertion in begining
for i in range(0, 5):
    temp = singLinkedList(i)
    if(head is None):
        head = temp
        continue
    temp.next = head
    head = temp

temp = head
print("Before Reversing")
while temp is not None:
    print(temp.val, end=' ')
    temp = temp.next

# Reverse Linked list
curr = head
pre = None
next = None
while curr is not None:
    next = curr.next
    curr.next = pre
    pre = curr
    curr = next

temp = pre
print("\nAfter Reversing")
while temp is not None:
    print(temp.val, end=' ')
    temp = temp.next
