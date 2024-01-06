class Node:
    def __init__(self, key):
        self.left = None
        self.val = key
        self.right = None
        
class BST():
    root = None
    def insert(self, item):
        node = Node(item)
        if self.root == None:
            self.root = node
            return
        
        current = self.root
        prev = None
        
        while current != None:
            if node.val == current.val:
                return current.val
            elif node.val > current.val:
                prev = current
                current = current.right
            else:
                prev = current
                current = current.left
                
        if node.val < prev.val:
            prev.left = node
        else:
            prev.right = node

    def display(self):
        current = self.root
        if current == None:
            print('the list is empty')
            return
        
        stack = []
        while current != None or len(stack) != 0:
            if current != None:    
                stack.append(current)
                current = current.left
            else:
                current = stack.pop()
                print(f'{current.val}', end = ' ')
                current = current.right
        print()
        
    def height(self):
        current = self.root
        prev = None
        height = 0
        while current != None:
            prev = current
            current = current.left
            height +=1
            if current == None:
                current = prev.right

        height = height - 1
        return print(height)

if __name__ == '__main__':
    x = BST()
    x.insert(10)
    x.insert(20)
    x.insert(30)
    x.insert(40)
    x.display()
    x.height()
    
# can print ra mot binary tree ma cac phan tu hien thi dung vi tri cua minh