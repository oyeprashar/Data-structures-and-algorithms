class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insertIntoBST(self, root, newData):
    
        if root is None:
            return Node(newData)

        if root.data > newData:
            root.left = self.insertIntoBST(root.left, newData)
        else:
            root.right = self.insertIntoBST(root.right, newData)

        return root
    
