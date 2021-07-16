class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right =None

def sizeRecursive(node):
    if node is None:
        return 0
    return (sizeRecursive(node.left) + 1 + sizeRecursive(node.right))

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)

print(sizeRecursive(root))