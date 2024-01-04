class Node:
    def __init__(self, value):
        self.val = value
        self.next = None
        

class Queue:
    def __init__():
        self.first = None
        self.last = None
        self.length = 0
        
    def peek():
        return self.first.val
        
    def enqueue(value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        
        self.length += 1
        return self
    
    def dequeue():
        if not self.first:
            return self

        if self.first == self.last:
            self.last = None
            
        this.first = this.first.next
        self.length -= 1
        return self