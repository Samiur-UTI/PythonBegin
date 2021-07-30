class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
class Que ():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    def peek(self):
        if (self.length == 0):
            print('Stack is empty')
        else: 
            print(self.first.value)
    def enqueue(self,value):
        newItem = Node(value)
        if (self.length == 0):
            self.first = newItem
            self.last = newItem
        else:
            holdingPosition = self.last
            self.last = newItem
            holdingPosition.next = newItem
        self.length += 1
    def dequeue(self):
        if(self.length == 0):
            return('Nothing to remove, que is empty')
        else: 
            holdingPosition = self.first.next
            self.first = holdingPosition
        self.length -= 1
    def printList(self):
        temp = self.first
        arr = []
        while (temp):
            arr.append(temp.value)
            temp = temp.next
        print(arr)
party = Que()
party.enqueue('Morty')
party.enqueue('Rick')
party.enqueue('Gwen')
party.printList()
party.peek()