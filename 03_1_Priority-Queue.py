class PriorityQueue:
    """
    Due to the dynamic properties of python list, we will try to restrict the amount of element in each queue manually
    However, we can always make use of this dynamic if we want to
    The whole point of Queue lie in the unique characteristic of enqueue and dequeue method FIFO natural
    """
    def __init__(self, capacity):
        self.maxSize = capacity
        self.data = [(None,None)] * capacity
        self.front = 0
        self.rear = 0
        self.size = 0
        
    def is_empty(self):
        return self.size == 0
    def is_full(self):
        return self.size == self.maxSize
    def get_size(self):
        return self.size
    def front(self):
        return self.front
    def rear(self):
        return self.rear
    
    def enqueue(self, priority, value):
        # Time Complexity: O(n) - Insertion sort approach
        if self.is_full():
            raise IndexError("Priority Queue is full")
        i = self.size - 1
        while i >= 0 and self.data[i][0] > priority:
            self.data[i + 1] = self.data[i]
            i -= 1
        self.data[i + 1] = (priority, value)
        self.size += 1

    def dequeue(self):
        # Time Complexity: O(1)
        if self.is_empty():
            raise IndexError("Dequeue from empty priority queue")
        value = self.data[0]
        for i in range(1, self.size):
            self.data[i - 1] = self.data[i]
        self.size -= 1
        self.data[self.size] = (None, None)
        return value
    
    def peek(self):
        if self.size == 0:
            raise IndexError("Queue is empty")
        return self.data[self.front]
    
    
        