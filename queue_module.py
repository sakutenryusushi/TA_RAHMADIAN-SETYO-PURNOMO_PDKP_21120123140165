from collections import deque

class Queue:
    def __init__(self):
        self.queue = deque()
    
    def enqueue(self, item):
        self.queue.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.queue.popleft()
        else:
            return None
    
    def is_empty(self):
        return len(self.queue) == 0
    
    def size(self):
        return len(self.queue)
    
    def get_all(self):
        return list(self.queue)
