class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def singly_linked_list_example(data):
    return Node(data)

head = None
tail = None

for i in range(1, 5):
    temp = singly_linked_list_example(i)
    if head is None:
        head = temp
        tail = temp
    else:
        tail.next = temp
        tail = temp

# Print the list
current = head
while current is not None:
    print(current.data, end=' ')
    current = current.next
