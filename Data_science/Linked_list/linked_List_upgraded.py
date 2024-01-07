
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Linked_list_upgraded:
    def __init__(self):
        self.head = None
        
    def is_Empty(self):
        return self.head is None
        
    def add_front(self, key):
        new_node = Node(key)
        new_node.next = self.head
        self.head = new_node
        
    def add_after(self, node, key):
        if node is None:
            print("Invalid node.")
            return
        new_node = Node(key)
        new_node.next = node.next
        node.next = new_node
        
    def pop_front(self):
        if self.is_empty():
            print("LinkedList is empty.")
            return None
        popped = self.head
        self.head = self.head.next
        popped.next = None
        return popped.data
        
    def pop_after(self, node):
        if node is None or node.next is None:
            print("Invalid node.")
            return None
        popped = node.next
        node.next = popped.next
        popped.next = None
        return popped.data
    
    def display(self):
        if self.is_Empty():
            print("LinkedList is empty.")
            return
        current = self.head
        while current:
            print(current.data, end= ' ')
            current = current.next
        print()
    
x = Linked_list_upgraded()
x.add_front(50)
x.add_front(40)
x.add_front(10)
x.add_after(x.head,20)
x.add_after(x.head.next,30)

x.display()

x.pop_after(x.head)
x.pop_after(x.head.next)

x.display()
