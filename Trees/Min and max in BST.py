class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def minNode(root):
    curr = root
    while curr.left is not None:  # we break form the loop when the node is the last left node and its left is None
        curr = curr.left
    return curr.data

def maxNode(root):
    curr = root
    while curr.right is not None:  # we break from the loop when the node is the last right node and its right is None
        curr = curr.right
    return curr.data

root = BST(8)
root.left = BST(3)
root.left.left = BST(1)
root.left.right = BST(6)
root.left.right.left = BST(4)
root.left.right.right = BST(7)
root.right = BST(10)
root.right.right = BST(14)
root.right.right.left = BST(13)
print("====MIN===")
print(minNode(root))
print("====MAX====")
print(maxNode(root))