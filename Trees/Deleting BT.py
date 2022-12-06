#LOGIC TO DELETE A BT
# We need to delete the children of a node before deleting that node
# This is can be achieved by post order traversing (Left, Right, Parent)

class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def deleteBT(node):
    
    if node != None:
        deleteBT(node.left)
        deleteBT(node.right)
        del node



