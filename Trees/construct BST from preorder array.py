
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def inorder(root):

    if root != None:
        inorder(root.left)
        print(root.data,end=" ")
        inorder(root.right)


def insertBST(root,key):

    if key < root.data:
        if root.left == None:
            root.left = Node(key)
        else:
            insertBST(root.left,key)

    if key > root.data:
        if root.right == None:
            root.right = Node(key)
        else:
            insertBST(root.right,key)

    return root
 
def constructBST(arr):

    root = Node(arr[0])

    for i in range(1,len(arr)):
        key = arr[i]

        root = insertBST(root,key)

    return root

    

arr = [10, 5, 1, 7, 40, 50]
root = constructBST(arr)
print(inorder(root))

