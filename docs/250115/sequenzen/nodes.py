# nodes.py

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
    def __str__(self):
        return f'{super().__str__()}\nValue: {self.value}\nNext: {self.next}'
        
    def set_next(self, next):
        self.next = next
        
class BNode:
    def __init__(self, value):
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        
    def __str__(self):
        return (
            f'\tParent: {self.parent if self.parent is None else self.parent.value}\n'
            f'\tValue: {self.value}\n'
            f'Left: {self.left if self.left is None else self.left.value}\t'
            f'Right: {self.right if self.right is None else self.right.value}'
        )
        
