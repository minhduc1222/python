# lam tren .py se nhanh hon

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linked_list:
    def __init__(self):
        self.head = None
        
    def is_Empty(self):
        return self.head is None
    
    def add_Item(self, item):
        new_node = Node(item)
        if self.is_Empty():
            self.head = new_node
        
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        
    def remove_Item(self, item):
        if self.is_Empty():
            print('the linked list is empty')
            return

        if self.head.data == item:
            self.head = self.head.next
            return
        
        current = self.head
        prev = None
        
        while current:
            if current.data == item:
                prev.next = current.next
                return
            prev = current
            current = current.next
            
        print(f'the item {item} is not on the list')
        
    def display(self):
        if self.is_Empty():
            print('the linked list is empty')
            return
        
        current = self.head
        
        while current:
            print(current.data, end = ' ')
            current = current.next
        print()

a_list = Linked_list()
a_list.add_Item(10)
a_list.add_Item(20)
a_list.add_Item(30)
a_list.add_Item(40)

a_list.display()

a_list.remove_Item(20)
a_list.remove_Item(30)

a_list.display()
