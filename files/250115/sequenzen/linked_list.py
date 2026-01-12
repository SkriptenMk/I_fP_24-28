# linked_list.py

from nodes import Node

class LinkedList:
    def __init__(self, value=None):
        self.length = 0
        if value:
            node = Node(value)
            self.head = node
            self.length += 1
        else:
            self.head = None
            
    def append(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node
        self.length += 1
        
    push = append
        
    def search(self, value):
        if self.head == None:
            return None
        
        node = self.head
        
        if node.value == value:
            return node
        
        while node.next:
            node = node.next
            if node.value == value:
                return node
            
        return None
    
    def delete(self, value):
        if self.head == None:
            return -1
        elif self.search(value) == None:
            return -1
        
        else:
            node = self.head
            if node.value == value:
                self.head = node.next
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
        
    def pop(self):
        if self.head is None:
            return -1
        else:
            node = self.head
            if node.next:
                node.next = None
            self.head = self.head.next
            return node
        
    def itrate(self):
        node = self.head
        while node:
            yield node.value
            node = node.next