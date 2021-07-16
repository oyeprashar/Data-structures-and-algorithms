class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printLeft(node,result):
    result.append(node.data)
    while(node.left != None):
        result.append(node.left.data)
        node = node.left
    return result

root = BinaryTree(12)
root.left = BinaryTree(10)
root.right = BinaryTree(20)
root.right.left = BinaryTree(25)
root.right.right = BinaryTree(40)
result = []
print(printLeft(root,result))