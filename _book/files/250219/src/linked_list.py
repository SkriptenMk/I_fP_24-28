class LinkedList:
    def __init__(self, value=None):
        self.length = 0
        if value:
            node = Node(value)
            self.root = node
            self.length += 1
        else:
            self.root = None
            
    def get_length(self):
        return self.length
            
    def append(self, value):
        node = Node(value)
        
        if self.root is None:
            self.root = node
            
        else:
            tmp = self.root
            self.root = node
            node.set_next(tmp)
            
        self.length += 1

        
    def search(self, value):
        if self.root == None:
            return None
        
        node = self.root
        
        if node.value == value:
            return node
        
        while node.connections['next']:
            node = node.connections['next']
            if node.value == value:
                return node
            
        return None
    
    def delete(self, value):
        if self.root == None:
            return -1
        elif self.search(value) == None:
            return -1
        
        else:
            node = self.root
            if node.value == value:
                self.root = node.connections['next']
                self.length -= 1
                return 0
            
            hook = node
            while node:
                if node.value == value:
                    hook.connections['next'] = node.connections['next']
                    self.length -= 1
                    return 0
                hook = node
                node = node.connections['next']
                
            return -1
        
