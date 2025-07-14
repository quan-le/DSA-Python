class HashTable:
    def __init__(self, capacity = 101, baseHash = 31):
        self.capacity = capacity
        self.baseHash = baseHash
        self.size = 0
        self.table = [[] for _ in range(capacity)] 
    
    def hashFunction(self, key):
        key_str = str(key)
        hash_value = 0
        for char in key_str:
            hash_value = (hash_value * self.baseHash + ord(char)) % self.capacity
        return hash_value

    def insert(self, key, value):
        """
        Time Complexity: O(1) average, O(n) worst-case (when all keys hash to the same bucket)
        """
        index = self.hashFunction(key)
        bucket = self.table[index]
        for i, (k, _) in enumerate(bucket):
            #the for loop give us both index i and key-value (k,_)
            if k == key:
                bucket[i] == (key,value)
                return
        bucket.append((key,value))
        self.size += 1
    
    def search(self, key):
        """
        Time Complexity: O(1) average, O(n) worst-case (when all keys hash to the same bucket)
        """
        index = self.hashFunction(key)
        bucket = self.table[index]
        for (k,v) in enumerate(bucket):
            if k == key:
                return v
        #raise KeyError(key + "Not exist")
        print(key + " not exist")
    
    def delete(self,key):
        """
        Time Complexity: O(1) average, O(n) worst-case (when all keys hash to the same bucket)
        """
        index = self.hashFunction(key)
        bucket = self.table[index]
        for i, (k,v) in enumerate(bucket):
            if k == key:
                del bucket[i]
                self.size -= 1
                return
        raise KeyError
    
    def __len__(self):
    # Time Complexity: O(1)
        return self.size
    
# Driver code

ht = HashTable()
ht.insert("apple", 3)
ht.insert("banana", 2)
ht.insert("cherry", 5)

print(ht.search("banana"))  # 2


ht.insert("banana", 4)
print(ht.search("banana"))  # 4


ht.delete("apple")
print(len(ht))  # 2

