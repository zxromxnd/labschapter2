class BiDirectionalPriorityQueue:
    def __init__(self):
        self.items = []
        self.counter = 0
    
    def enqueue(self, item, priority):
        self.items.append({
            'item': item,
            'priority': priority,
            'order': self.counter
        })
        self.counter += 1

    def size(self):
        return len(self.items)
    
    def is_empty(self):
        return len(self.items) == 0