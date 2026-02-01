# nodes.py

class Node:
    def __init__(self, value):
        self.value = value
        self.connections = {
            'next': None
        }
        
    def __str__(self):
        s = f'Value: {self.value}\n'
        s += 'Next: None' if self.connections['next'] is None else f'Next: {str(self.connections['next'].value)}'
        
        return s
        
    def set_next(self, next):
        self.connections['next'] = next
