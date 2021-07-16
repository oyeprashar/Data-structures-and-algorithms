# MIRROR OR SYMMETRIC TREES
# ===LOGIC====
# Base case is when both root1 and root2 are None we return True
# Recursion explanation:
# If root1 and root2 are not None and if root.data == root2.data we recursively compare
# the left with right and right with left and if their data matches the recursion happens
# if we are able to recursively traverse the tree then return True
# FOR FALSE: if root1 and root2 are not None and neither there their datas are equal then False is returned
class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def mirror(root):
    return getMirror(root,root)

def getMirror(root1,root2):
    if root1 is None and root2 is None:
        return True

    if root1 is not None and root2 is not None:
        if root1.data == root2.data:
            return getMirror(root1.left,root2.right) and getMirror(root1.right,root2.left)
    return False

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(2)
root.left.left = BinaryTree(3)
root.left.right = BinaryTree(4)
root.right.left = BinaryTree(4)
root.right.right = BinaryTree(3)

print(mirror(root))