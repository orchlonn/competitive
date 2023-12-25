# designing stack using linked list
class Node:
    def __init__(self, data):
       self.data = data
       self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0
    
    def peek():
        return self.top.value
    
    def push(value):
        newNode = Node(value)
        if length == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            holdinPointers = self.top
            self.top = newNode
            self.top.next = holdinPointers
        
        self.length += 1
        
    def pop():
        if not self.top:
            return None
        
        if self.top == self.bottom:
            self.bottom = None

        self.top = self.top.next
        self.length -= 1
        
        
        