class Node:
    def __init__(self, data, pre, next):
        self.pre = None
        self.data = data
        self.next = None

def DoublyLinkedList(data):
    return Node(data)

head = None
tail = None

for i in range(0, 6):
    temp = DoublyLinkedList(i)
    if head == None and tail == None:
        head = temp
        temp.pre = head
        temp.next = tail
        tail = temp
    else:
        
