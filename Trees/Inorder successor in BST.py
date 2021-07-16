class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def minVal(node):
    current = node
    while current.left is not None:
        current = current.next
    return current.data

def inorderSuccessor(root,node):
    if node.right is not None:
        return minVal(node.right)

    successor = None
    while(root):
        if node.data > root.data:
            root = root.right

        elif node.data < root.data:
            successor = root
            root = root.left

        else:
            break
    return successor.data

root = BST(50)
root.left = BST(16)
root.left.left = BST(14)
root.left.left.left = BST(10)
root.left.left.left.left = BST(5)
root.left.left.right = BST(15)
root.left.right = BST(40)
root.left.right.right = BST(45)
root.left.right.left = BST(35)
root.left.right.left.left = BST(32)
root.left.right.left.left.left = BST(30)
root.left.right.left.right = BST(36)
root.left.right.left.right.right = BST(37)
root.right = BST(90)
root.right.left = BST(80)
root.right.left.left = BST(75)
root.right.left.right = BST(82)
root.right.left.right.left = BST(81)
root.right.left.right.right = BST(85)
root.right.left.right.right.right = BST(87)
root.right.right = BST(100)
root.right.right.right = BST(105)

print(inorderSuccessor(root,root.left.right.left.right.right))
print(inorderSuccessor(root,root.left.left.right))
print(inorderSuccessor(root, root.right.right))