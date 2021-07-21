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
    def traverse(self,index):
        counter = 0
        currentNode = self.head
        while(counter != index):
            currentNode = currentNode.next
            counter += 1
        return currentNode
    def insert(self,index,value):
        if(index >= self.length):
            return self.append(value)
        else: 
            newNode = Node(value)
            leadIndex = self.traverse(index -1)
            nextIndex = leadIndex.next
            leadIndex.next = newNode
            newNode.next = nextIndex
            self.length += 1
            return self.printList()
    def remove(self, index):
        leadIndex = self.traverse(index-1)
        nextIndex = leadIndex.next
        leadIndex.next = nextIndex.next
        self.length -= 1
        return self.printList()
    def printList(self):
        temp = self.head
        arr = []
        while (temp):
            arr.append(temp.value)
            temp = temp.next
        print(arr)
    
alpha = LinkedList(2)
alpha.append(10)
alpha.prepend(15)
alpha.insert(2,44)
alpha.remove(2)

