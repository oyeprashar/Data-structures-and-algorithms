class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    def insertLeft(self,newData):
        if self.left == None:
            self.left = BinaryTree(newData)
        else:
            t = BinaryTree(newData)
            t.left = self.left 
            self.left = t

    def insertRight(self,newData):
        if self.right == None:
            self.right  = BinaryTree(newData)
        else:
            t = BinaryTree(newData)
            t.right = self.right
            self.right = t

    def getRightChild(self):
        return self.right.data
        
    def getLeftChild(self):
        return self.left.data

    def getParent(self):
        return self.data





root_node = BinaryTree(11)
root_node.left = BinaryTree(22)
root_node.right = BinaryTree(33)
print(root_node.getParent())
print(root_node.getLeftChild())
print(root_node.getRightChild())
