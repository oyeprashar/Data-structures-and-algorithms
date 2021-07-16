
class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def recursiveSearch(node,key):
    if node is None:
        return 0
    if node.data == key:
        return 1

    else:
        # temp is set to 1 if element is found in left or right subtree
        temp = recursiveSearch(node.left,key) or recursiveSearch(node.right, key)
        if temp == 1:
            return temp

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)

print(recursiveSearch(root, 3))

