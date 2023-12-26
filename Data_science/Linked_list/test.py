class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linked_List:
    def __init__(self):
        self.head = None
        
    def is_Empty(self):
        return self.head is None
    
    def add_item(self, item):
        new_item = Node(item)
        if self.is_Empty():
            self.head = new_item
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_item
        
    def remove_item(self, item):
        new_item = Node(item)
        if self.is_Empty():
            print('the linked list is empty')
        if self.head == new_item:
            self.head = self.head.next
            
        current = self.head
        prev = None
        
        while current:
            if current.data == item:
                prev.next = current.next
                return
            prev = current
            current = current.next
            
    def display(self):
        if self.is_Empty():
            print('the linked list is empty')
        
        current = self.head
        while current:
            print(current.data, end= ' ')
            current = current.next
        print()
x = Linked_List()
x.add_item(10)
x.add_item(20)
x.add_item(30)

x.display()

x.remove_item(20)

x.display()

