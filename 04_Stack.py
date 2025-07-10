class Stack:
    """
    Stack follow LIFO (Last In First Out)
    The key work we have with stack is to keep track of top variables. Top will follow the last inserted var
    """
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.data = [None] * capacity
        self.top = -1
    
    def getCapacity(self):
        return self.capacity
    def isEmpty(self):
        return self.top == -1
    def isFull(self):
        return self.top == self.capacity -1
    
    def push(self, value):
        if self.isFull():
            raise OverflowError("the Stack is full")
        else:
            self.top += 1
            self.data[self.top] = value
    
    def pop(self):
        if self.isEmpty():
            raise IndexError("the Stack is empty")
        else:  
            item = self.data[self.top]
            self.top -= 1
            return item
        
    def peek(self):
        if self.isEmpty():
            raise IndexError("the Stack is empty")
        return self.data[self.top]
    
    def getSize(self):
        return self.top + 1
    
    def clear(self):
        """clear or reset the stack"""
        self.top = -1
        
#-------
# Example Usage
if __name__ == "__main__":
    s = Stack(capacity=10)
    s.push(10)
    s.push(20)
    s.push(30)
    print("Stack after pushes:", s.data[:s.getSize()])
    print("Peek:", s.peek())
    print("Pop:", s.pop())
    print("Stack after pop:", s.data[:s.getSize()])
    print("Is Empty:", s.isEmpty())
    print("Size:", s.getSize())
    s.clear()
    print("Stack after clear:", s.data[:s.getSize()])