class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        new_node = Node(value)
        left_node = self.tail.prev
        
        left_node.next = new_node
        new_node.prev = left_node
        new_node.next = self.tail
        self.tail.prev = new_node

    def appendleft(self, value: int) -> None:
        new_node = Node(value)
        first_node = self.head.next

        new_node.next = first_node
        first_node.prev = new_node
        new_node.prev = self.head
        self.head.next = new_node
        

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        last_node = self.tail.prev
        value = last_node.val
        prev_node = last_node.prev

        prev_node.next = self.tail
        self.tail.prev = prev_node

        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        first_node = self.head.next
        value = first_node.val
        next_node = first_node.next

        next_node.prev = self.head
        self.head.next = next_node

        return value
