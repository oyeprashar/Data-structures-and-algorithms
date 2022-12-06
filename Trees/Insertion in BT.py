class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def insertLeft(self, newData):
        if self.left is None:
            self.left = BinaryTree(newData)
        else:
            t = BinaryTree(newData)
            t.left = self.left
            self.left = t

    def insertRight(self, newData):
        if self.right is None:
            self.right = BinaryTree(newData)
        else:
            t = BinaryTree(newData)
            t.right = self.right
            self.right = t

