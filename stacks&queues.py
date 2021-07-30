class Node():
    def __init__(self,value):
        self.value = value
        self.next = None
class Stack ():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    def peek(self):
        return self.top
    def push (self,value):
        newItem = Node(value)
        if (self.length == 0):
            self.top = newItem
            self.bottom = newItem
        else: 
            holdingPosition = self.top
            self.top = newItem
            newItem.next = holdingPosition
        self.length += 1
        return self.printList()
    def pop (self):
        if (self.length == 0):
            return None
        else: 
            newTop = self.top.next
            self.top = newTop
            self.length -= 1
            return self.printList()
    def printList(self):
        temp = self.top
        arr = []
        while (temp):
            arr.append(temp.value)
            temp = temp.next
        print(arr)
myStack = Stack()
myStack.push('hola')
myStack.push('Google')
myStack.push('Amazon')
myStack.pop()
