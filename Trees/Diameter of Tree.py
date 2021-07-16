class BinaryTree():
    def __init__(self, data):
        self.data= data
        self.left = None
        self.right = None

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left),height(node.right))

def diameter(node1):
    if node1 is None:
        return 0
    lheight = height(node1.left)
    rheight = height(node1.right)

    ldiameter = diameter(node1.left)
    rdiameter = diameter(node1.right)

    return max(lheight+rheight+1, max(ldiameter,rdiameter))

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)

print(diameter(root))