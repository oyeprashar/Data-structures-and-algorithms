class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def heightBT(node):
    if node is None:
        return 0

    return 1 + max(heightBT(node.left),heightBT(node.right))

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)

print(heightBT(root))