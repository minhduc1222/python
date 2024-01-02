# implement the insertion operation iteratively
class GFG:
    @staticmethod
    def main(args):
        tree = BST()
        tree.insert(30)
        tree.insert(50)
        tree.insert(15)
        tree.insert(20)
        tree.insert(10)
        tree.insert(40)
        tree.insert(60)
        tree.inorder()

class Node: # those attribute's used by all instances in class BST( does not belong to a specific instance) -> not be put within __init__
    left = None
    val = 0
    right = None
    
    def __init__(self, val):
        self.val = val
        
class BST:
    root = None
    
    # function to insert key into the binary tree
    def insert(self, key):
        node = Node(key)
        if (self.root == None):
            self.root = node
            return
        prev = None
        temp = self.root
        while(temp!=None):
            if key < temp.val:
                prev = temp
                temp = temp.left
            elif key > temp.val:
                prev = temp
                temp = temp.right
        
        if key < prev.val:
            prev.left = node
        elif key > prev.val:
            prev.right = node
                
    # function to print the traversal order
    def inorder(self):
        temp = self.root
        stack = []
        while ((temp != None) or not (len(stack) == 0)):
            if temp != None:
                stack.append(temp)
                temp = temp.left
            else:
                temp = stack.pop()
                print(str(temp.val) + ' ', end = ' ')
                temp = temp.right

if __name__ == "__main__":
    GFG.main([])
 