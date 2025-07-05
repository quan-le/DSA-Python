class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next                                    #Pointer to another Node datatype
        
    def get_data(self):
        return self.data
    
    def set_data(self, data):
        self.data = data
        
    def get_next(self):
        return self.next
    
    def set_next(self, next):
        self.next = next

class CircularLinkedList: 
    """
    The important detail we have to pay attention to working with circular linked list is when doing append, delete or 
    other operation with the head and tail of linked list, we have to make sure to open and close the loop.
    The tail of circular linked list change from none to Pointer to the head.
    We also keep track of the tail of the linked list. This give us the advantage of not having to transverse to the whole list
    """
    def __init__(self):
        self.head : Node = None
        self.tail : Node = None
        self.size = 0
        
    def is_empty(self):
        return self.head is None
    
    def append(self, node):
        '''
        Complexity : O(1)
        '''
        if self.is_empty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            node.next = self.head
            self.tail = node
        self.size += 1
    
    def prepend(self, node):
        '''
        Time Complexity: O(1)
        '''
        if self.is_empty():
            self.head = self.tail = node
        else:
            node.next = self.head
            self.tail.next = node
            self.head = node
        self.size += 1
    
    def insert(self, index, node):
        '''
        Time Complexity: O(n) or O(1) if we insert at index 0
        '''
        if not 0 <= index <= self.size:
            raise IndexError("Index out of bound")
        if index == 0:  
            self.prepend(node)
        else:
            current = self.head
            for i in range(index - 1):
                current = current.next
            node.next = current.next
            current.next = node
            self.size += 1
        
    def searchNode (self, node):
        '''
        Time Complexity: O(n)
        '''
        current = self.head
        index = 0
        while (current.next is not None ):
            if(current != node):
                current = current.next
                index += 1
            else:
                return index
        return -1                                           #node does not exist in this linkedList
    
    def searchValue(self, node_value):
        '''
        Time Complexity: O(n)
        '''
        current = self.head
        while(current.next is not None):
            if(current.data != node_value):
                current = current.next
            else:
                return current
        return -1
    
    def deleteNode(self, node):
        '''
        Time Complpexity O(n)
        '''
        current = self.head
        while(current.next is not None):
            if(current != node):
                current = current.next
            else:
                current.next = current.next.next
                self.size -= 1
        self.tail.next = self.head
        return -1