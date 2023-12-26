
class Hash_Table:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]
        
    def _hash_function(self, key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        index = self._hash_function(key)
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
        for i, item in enumerate(self.table[index]):
            if item[0] == key:
                del self.table[index][i]
                return 
    def display(self):
        for index in range(self.size):
            print(f'index {index}: ', end= ' ')
            for item in self.table[index]:
                print(f'{item[0]}: {item[1]}', end=' -> ')
            print(None)
                

x = Hash_Table(10)
x.insert('apple', '3')
x.insert('light', '6')

x.display()

x.remove('apple')

x.display()
