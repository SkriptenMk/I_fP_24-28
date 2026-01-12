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
        
class DNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.connections['previous'] = None
        
    def __str__(self):
        s = 'Prvious: None\n' if self.connections['previous'] is None else f'Previous: {str(self.connections['previous'].value)}\n'       
        s +=  super().__str__()
        return s
    
    def set_previous(self, prev):
        self.connections['previous'] = prev