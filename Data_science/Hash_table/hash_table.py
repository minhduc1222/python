class Hash_table:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def _hash_function(self, key): 
        return hash(key) % self.size # hash(): return a unique integer value to compare(distinguish) between dictionary keys, for dict look-up functions
    
    def insert(self, key, value):
        index = self._hash_function(key) # invoke hash() ->generate a hash value for the given key, apply modulus to it to limit it to the table size
        for item in self.table[index]:
            if item[0] == key:
                item[1] = value
                return 
        self.table[index].append([key, value])
        
    def get(self, key):
        index = self._hash_function(key)
        for item in self.table[index]:
            if item[0] == key:       
                return item[1]
        return None
    
    def remove(self, key):
        index = self._hash_function(key)
        for i, item in enumerate(self.table[index]): # keep track of number of iteration within a loop, by initiating a value that changes along with iterable object
            if item[0] == key:  # return each element as enumerate object
                del self.table[index][i]
                return
            
    def display(self):
        for index in range(self.size):
            print(f"index {index}: ", end=' ')
            for item in self.table[index]:
                print(f'{item[0]}: {item[1]}', end=' -> ')
            print('None')
            
x = Hash_table(10)
x.insert('apple', 'a')
x.insert('banana', 'b')
print(x.get('apple'))
print(x.get('banana'))

x.display()


