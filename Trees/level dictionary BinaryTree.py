class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

def getLevel(root,dict1,level):
    if root is None:
        return
    dict1.setdefault(level, [])
    dict1[level].append(root.data)

    getLevel(root.left,dict1,level+1)
    getLevel(root.right,dict1,level+1)

    return dict1

dict1 = {}
level = 1
root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(7)
root.left.right = BinaryTree(6)
root.right.left = BinaryTree(5)
root.right.right = BinaryTree(4)

print(getLevel(root,dict1,level))
