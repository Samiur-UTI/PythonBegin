class LinkedList ():
    def __init__ (self,value):
        self.head = {
            value: value,
            next: None
        }
alpha = LinkedList(2)
print(alpha)