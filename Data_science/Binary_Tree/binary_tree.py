# binary tree: Tree that each node only has a maximum number of children equal to 2
#       22
#      /   \
#     8    32
#    / \   /  \
#   1  10 30  43
#    \   \  \   \
#     5  20 31  49


class Node:
    def __init__(self, key):
        self.right = None
        self.left = None
        self.val = key
        
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

# do an inorder tree traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=' ')
        inorder(root.right)
        
#driver program to test the above functions
if __name__ == "__main__":
# the following BST
    #     50
    #   /    \
    #  30    70
    # /  \   / \
    # 20 40 60 80
    
    r = Node(50)
    r = insert(r,20)
    r = insert(r,40)
    r = insert(r,30)
    r = insert(r,70)
    r = insert(r,60)
    r = insert(r,80)
    
    
    inorder(r)