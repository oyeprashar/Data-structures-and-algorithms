class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right= None

def findNode(root, key):
    if root is None or root.data == key:
        return root
    if root.data < key:
        return findNode(root.right, key)
    if root.data > key:
        return findNode(root.left, key)

root = BST(8)
root.left = BST(3)
root.left.left = BST(1)
root.left.right = BST(6)
root.left.right.left = BST(4)
root.left.right.right = BST(7)
root.right = BST(10)
root.right.right = BST(14)
root.right.right.left = BST(13)

ans = findNode(root,1)
print(ans.data)