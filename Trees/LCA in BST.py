class BST:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def LCA(root,n1,n2):
    if root.data > n1 and root.data > n2:
        return LCA(root.left,n1,n2)

    if root.data < n1 and root.data < n2:
        return LCA(root.right,n1,n1)
        
    else:
        return root.data

root = BST(5)
root.left = BST(4)
root.left.left = BST(3)
root.right = BST(6)
root.right.right = BST(7)
root.right.right.right = BST(8)

print(LCA(root,7,8))