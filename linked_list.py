class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
class LinkedList ():
    def __init__ (self,value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1
    def append(self,value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1
    def prepend(self,value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1

alpha = LinkedList(2)
print(alpha)
alpha.append(10)
print(alpha.head)
alpha.prepend(15)
print(alpha)