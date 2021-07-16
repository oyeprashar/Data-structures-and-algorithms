class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
def getLevel(node, key, level):
    if node is None:
        return 0
    if node.data == key:
        return level
    downlevel = getLevel(node.left,key,level+1)
    if downlevel != 0:
        return downlevel

    downlevel = getLevel(node.right,key,level+1)
    return downlevel

root = BinaryTree(3)
root.left = BinaryTree(2)
root.right = BinaryTree(5)
root.left.left = BinaryTree(1)
root.left.right = BinaryTree(4)
level = 0
print(getLevel(root,1,level))
print(getLevel(root,2,level))
print(getLevel(root,3,level))
print(getLevel(root,4,level))
print(getLevel(root,5,level))