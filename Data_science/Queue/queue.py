class Queue:
    def __init__(self):
        self.item = []
        
    def is_Empty(self):
        return self.item is None
    
    def enqueue(self, value):
        self.item.append(value)
        
    def dequeue(self):
        if not self.is_Empty():
            return self.item.pop(0)
        else:
            print('the queue is empty')
            
    def peek(self):
        if not self.is_Empty():
            return self.item[0]
        else:
            print('the queue is empty')
            
    def display(self):
        for i in range(len(self.item)):
            print(self.item[i], end = ' ')
        print()
        
    def size(self):
        return len(self.item)
    
x = Queue()
x.display()
x.enqueue(10)
x.enqueue(20)
x.enqueue(30)

x.display()

x.dequeue()

x.display()
