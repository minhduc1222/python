class Main:
    @staticmethod
    def main(arg):
        tree = BST() # Binary search tree
        tree.insert(50)
        tree.insert(30)
        tree.insert(15)
        tree.insert(50)
        tree.insert(20)
        tree.insert(10)
        tree.insert(40)
        tree.insert(60)
        tree.in_order()


class Node:
    val = 0
    def __init__(self, val):
        self.left = None
        self.val = val
        self.right = None


class BST:
    root = None

    def insert(self, key):
        node = Node(key)
        if self.root == None:
            self.root = node
            return
        
        prev = None
        temp = self.root
        while temp != None:
            if key < temp.val:
                prev = temp
                temp = temp.left
            elif key > temp.val:
                prev = temp
                temp = temp.right
            elif key == temp.val:
                return temp
        if key < prev.val:
            prev.left = node
        elif key > prev.val:
            prev.right = node
    def in_order(self):
        temp = self.root
        stack = []

        while ((temp != None) or not (len(stack) == 0)):
            if temp != None:
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                print(temp.val, end=' ')
                temp = temp.right


if __name__ == '__main__':
    Main.main([])