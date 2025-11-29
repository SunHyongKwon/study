class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0

    def enqueue(self, val):
        self.items.append(val)

    def dequeue(self):
        if self.front_index == len(self.items):
            return None
        val = self.items[self.front_index]
        self.front_index += 1
        return val

    def is_empty(self):
        return self.front_index == len(self.items)
    
    def size(self):
        return len(self.items) - self.front_index