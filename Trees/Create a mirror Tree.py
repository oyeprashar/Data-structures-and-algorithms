class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None 

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)

def createMirror(root1):

    if root1 == None:
        return None 

    root2 = Node(root1.data) 
    root2.left = createMirror(root1.right)
    root2.right = createMirror(root1.left)

    return root2 

# root = Node(5)
# root.left = Node(3)
# root.left.left = Node(2)
# root.left.right = Node(4)
# root.right = Node(6)

root = Node(2)
root.left = Node(1)
root.left.left = Node(12)
root.right = Node(8)
root.right.right = Node(9)

inorder(root)
print()

root2 = createMirror(root)

inorder(root2)



