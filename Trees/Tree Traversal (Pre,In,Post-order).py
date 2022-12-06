class BinaryTree():
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    
    def insertLeft(self,newData):
        if self.left == None:
            self.left = BinaryTree(newData)
        else:
            t = BinaryTree(newData)
            t.left = self.left
            self.left = t

    def insertRight(self, newData):
        if self.right == None:
            self.right = BinaryTree(newData)
        else:
            t = BinaryTree(newData)
            t.right = self.right
            self.right = t

# Pre-order/In-order/Post-order are implemeneted as external functions, not as a part of the class
def printPreorder(node): #PLR
    if node:
        print(node.data)
        printPreorder(node.left)
        printPreorder(node.right)
   

def printInorder(node): #LPR
    if node:
        printInorder(node.left)
        print(node.data)
        printInorder(node.right)
    


def printPostorder(node): #LRP
    if node:
        printPostorder(node.left)
        printPostorder(node.right)
        print(node.data)
    

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)

print("====PRE-ORDER TRAVERSAL====")
printPreorder(root)

#printing a blank line
print()

print("====IN-ORDER TRAVERSAL====")
printInorder(root)

#printing a blank line
print()

print("====POST-ORDER TRAVERSAL====")
printPostorder(root)

