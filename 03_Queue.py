class Queue:
    """
    Due to the dynamic properties of python list, we will try to restrict the amount of element in each queue manually
    However, we can always make use of this dynamic if we want to
    The whole point of Queue lie in the unique characteristic of enqueue and dequeue method FIFO natural
    """
    def __init__(self, capacity):
        self.maxSize = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        
    def is_empty(self):
        return self.size == 0
    def size(self):
        return self.size
    def front(self):
        return self.front
    def rear(self):
        return self.rear
    
    def enqueue(self, value):
        if self.size == self.maxSize:
            raise IndexError("Reach maximum capacity")
        if self.size == 0:
            self.data[self.rear] = value
            self.front += 1
            self.rear += 1
        else:
            self.data[self.rear] = value
            self.rear  += 1
        self.size += 1
        
    def dequeue(self):
        if self.size == 0:
            raise IndexError("Queue is empty")
        else:
            value = self.data[self.front]
            self.data[self.front] = None
            self.front += 1
            self.size -= 1
            return value
    
    def peek(self):
        if self.size == 0:
            raise IndexError("Queue is empty")
        return self.data[self.front]
    
    
        