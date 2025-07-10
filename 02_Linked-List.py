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
        
class LinkedList: 
    def __init__(self):
        self.head : Node = None
        self.size = 0
        
    def is_empty(self):
        return self.head is None
    
    def get_tail(self, node):
        previous = node
        current = previous.next
        if current.next is None:
            return current
        else:
            self.transverse(self, current)
    
    def append(self, node: Node):
        '''
        Complexity : O(N)
        '''
        if self.is_empty():
            self.head = node
        else:
            current_node = self.head
            while(current_node is not None and current_node.next is not None):
                current_node = current_node.next
            current_node.next = node
        self.size += 1
    
    def prepend(self, node):
        '''
        Time Complexity: O(1)
        '''
        if self.is_empty():
            self.head = node
        else:
            previous_head = self.head
            node.next = previous_head
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
        Time Complpexity O()
        '''
        current = self.head
        while(current.next is not None):
            if(current != node):
                current = current.next
            else:
                current.next = current.next.next
                self.size -= 1
        return -1
    
linked_list = LinkedList()
node1 = Node(43)
node2 = Node(0)
node3 = Node(1)
linked_list.append(node1)
linked_list.append(node2)
linked_list.append(node3)