
class Stack:
    def __init__(self):
        self.item = []
    
    def is_Empty(self):
        return self.item is None
    
    def push(self, value):
        self.item.append(value)
        
    def pop(self):
        if not self.is_Empty():
            return self.item.pop()
        else:
            print('The stack is empty')
            
    def peek(self):
        if not self.is_Empty():
            return self.item[-1]
        else:
            print('The stack is empty')
            
    def display(self):
        for i in range(len(self.item)):
            print(self.item[i], end=' ')
        print()
        
    def size(self):
        return len(self.item)
    
        
x = Stack()
x.push(10)
x.push(20)
x.push(30)

x.display()

print(x.peek())

x.pop()
x.display()
