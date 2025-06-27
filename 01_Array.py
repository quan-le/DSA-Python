class Array:
    def __init__(self, len):
        if (len < 0):
            raise ValueError("The length of Array must be a positive interger")
        self.len = len
        self.data = [None] * len
        
    def __len__(self):
        return self.len
    
    def __str__(self):
        return str([self.data[i] for i in range(self._size)])
    
    def __checkIndexValid(self, index):
        return 0 <= index < self.len        
    
    def get(self, index):
        if self.__checkIndexValid(index) == True:
            return self.data[index]
        else:
            raise IndexError("Index out of bound")
    
    def set(self, index, value):
        if self.__checkIndexValid(index) == True:
            self.data[index] = value
        else:
            raise IndexError("Index out of bound")
    
    def search(self, value):
        for i in range(self.len):
            if self.data[i] == value:
                return i                                        # The first index of value
            else:
                return -1                                       # Value doesn't exist              
    
    def add(self , value , index=None):
        if index == None:
            self.data[index] = value
            
        else:
            for i in range(self.len, index, -1):
                self.data[i] = self.data[i + 1]                 # shift data to the right
            self.data[index] = value              
        
        self.size += 1
        
    def remove(self , index):
        if self.__checkIndexValid(index) == False:
            raise IndexError("Index out of bound")
        else:
            for i in range(index, self.len - 1): 
                self.data[i] = self.data[i + 1]                 # shift data from the right of index to the left
            self.data[self.len - 1] = None                      # Delete the last data and resize
            self.len -= 1