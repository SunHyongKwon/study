class Stack:
    def __init__(self):
        self.items = []

    def push(self, val):
        self.items.append(val)
    
    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            return None
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            return None
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    