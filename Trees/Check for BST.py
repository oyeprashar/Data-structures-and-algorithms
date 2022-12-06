INT_MIN = -2 ** 38  # initializing variable before a function makes it global and we can use it in the function like a global variable
INT_MAX = 2 ** 38   # without  passing it as an argument to the function


## checking if given tree is a BST
class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def isBst(root):
    return getisBST(root, INT_MIN, INT_MAX)


def getisBST(node, mini, maxi):
    if node is None:  # if we have traversed all nodes and encountering None then return True
        return True  # also an empty tree is a BST         

    # checking the condition for each node
    if node.data <= mini or node.data >= maxi:
        return False

    return getisBST(node.left, mini, node.data) and getisBST(node.right, node.data, maxi)


# root = BST(4) # EXPECTED = CURRENT = True
# root.left = BST(2)
# root.right = BST(5)
# root.left.left = BST(1)
# root.left.right = BST(3)
# print(isBst(root))


root = BST(2) # this is a False case
root.right = BST(7)
root.right.right = BST(6)
root.right.right.right = BST(6)
root.right.right.right.right = BST(5)
root.right.right.right.right.right = BST(9)
print(isBst(root))
