class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linked_List_Upgraded:
    def __init__(self):
        self.head = None
        
    def is_Empty(self):
        return self.head is None
    
    def add_front(self,item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
    
    def add_after(self, node, item):
        new_node = Node(item)
        if node is None:
            print('invalid node')
            return
        new_node.next = node.next
        node.next = new_node

    def pop_front(self):
        if self.is_Empty():
            print('the linked list is empty')
            return None
        else:
            popped = self.head
            self.head = self.head.next
            popped.next = None
            return
        
    def pop_after(self, node):
        if self.is_Empty():
            print('the linked list is empty')
            return None
        if node is None or node.next is None:
            print('invalid node')
            return None
        
        popped = node.next
        node.next = popped.next
        popped.next = None
        return popped.data
    
    def display(self):
        if self.is_Empty():
            print('the linked list is empty')
            return
        
        current = self.head
        while current:
            print(current.data, end= ' ')
            current = current.next
        print()
        
x = Linked_List_Upgraded()
x.add_front(20)
x.add_after(x.head, 30)
x.add_front(10)

x.display()

x.pop_front()
x.pop_after(x.head)
x.display()
