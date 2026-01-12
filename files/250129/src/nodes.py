# nodes.py

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return f'{super().__str__()}\nValue: {self.value}\nNext: {self.next}'
        
    def set_next(self, next):
        self.next = next
        
class QNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.prev = None
        
    def __str__(self):
        msg = (f'Previous: {None if self.prev is None else self.prev.value}\n'      
               f'Value: {self.value}\n'
               f'Next: {None if self.next is None else self.next.value}')
        return msg