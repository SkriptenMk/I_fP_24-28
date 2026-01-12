# linked_list.py

from nodes import Node, QNode

class LinkedList:
    def __init__(self, value=None):
        self.length = 0
        if value:
            node = Node(value)
            self.tail = node
            self.length += 1
        else:
            self.tail = None
            
    def append(self, value):
        node = Node(value)
        node.next = self.tail
        self.tail = node
        self.length += 1
        
    push = append
    
    def pop(self) -> Node:
        result = self.tail
        self.tail = result.next
        result.next = None
        self.length -= 1
        return result
        
    def search(self, value):
        if self.tail == None:
            return None
        
        node = self.tail
        
        if node.value == value:
            return node
        
        while node.next:
            node = node.next
            if node.value == value:
                return node
            
        return None
    
    def delete(self, value):
        if self.tail == None:
            return -1
        elif self.search(value) == None:
            return -1
        
        else:
            node = self.tail
            if node.value == value:
                self.tail = node.next
                self.length -= 1
                return 0
            
            hook = node
            while node:
                if node.value == value:
                    hook.next = node.next
                    self.length -= 1
                    return 0
                hook = node
                node = node.next
                
            return -1
                
    def itrate(self):
        node = self.tail
        while node:
            yield node.value
            node = node.next
            
class Queue(LinkedList):
    def __init__(self, value=None):
        super().__init__(value)
        if value:
            node = QNode(value)
            self.tail = node
            self.head = node
            self.length += 1
            
        else:
            self.head = None
            self.tail = None
            
    def append(self, value):
        node = QNode(value)
        prev_node = self.tail
        self.tail = node
        node.next = prev_node
        prev_node.prev = self.tail
        self.length += 1
        
    def pop(self):
        node = self.head
        self.head = node.prev
        node.prev = None
        node.next = None
        self.length -= 1
        return node
        