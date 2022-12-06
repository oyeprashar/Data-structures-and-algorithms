"""
Insertion in a Binary Tree in level order
"""

class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):

    if root != None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)


def levelOrderInsertion(root,newData):
    if root == None:
        return BinaryTree(newData)

    newNode = BinaryTree(newData)
    queue = [root]

    while len(queue) != 0:

        curr = queue.pop(0)

        if curr.left == None:
            curr.left =  newNode
            return root

        else:
            queue.append(curr.left)

        if curr.right == None:
            curr.right = newNode
            return root

        else:
            queue.append(root.right)


    
root = BinaryTree(10)
root.left = BinaryTree(11)
root.left.left = BinaryTree(7)
root.right = BinaryTree(9)
root.right.left = BinaryTree(15)
root.right.right = BinaryTree(8)

inorder(root)

root = levelOrderInsertion(root,12)
print("\n---- AFTER ----")
inorder(root)