class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def heightCheck(node):
    if node is None:
        return 0
    return max(heightCheck(node.left),heightCheck(node.right))+1

def checkHeightBalance(node):
    l = heightCheck(node.left)
    r = heightCheck(node.right)
    if l-r == 1 or l-r == -1:
        return 1
    else:
        return 0

# # Balanced tree | Expected O/P -> 1
root = BinaryTree(1)
root.left = BinaryTree(10)
root.left.left = BinaryTree(5)
root.right = BinaryTree(39)

# # Unbalanced tree | Expected O/P -> 0
# root = BinaryTree(1)
# root.left = BinaryTree(2)
# root.left.right = BinaryTree(3)

print(checkHeightBalance(root))