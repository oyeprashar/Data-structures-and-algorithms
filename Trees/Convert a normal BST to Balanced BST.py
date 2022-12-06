class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def getInorder(root,arr):

    if root:
        getInorder(root.left,arr)
        arr.append(root.data)
        getInorder(root.right,arr)

def printPreOrder(root):

    if root:
        print(root.data,end =" ")
        printPreOrder(root.left)
        printPreOrder(root.right)

def buildTree(left,right,arr):

    if left > right:
        return None

    mid = (left + right) // 2

    currNode = Node(arr[mid])

    currNode.left = buildTree(left,mid-1,arr)
    currNode.right = buildTree(mid+1,right,arr)

    return currNode

def getNewRoot(root):

    arr = []
    getInorder(root,arr)

    return buildTree(0,len(arr)-1,arr)



# root = Node(4)
# root.left = Node(3)
# root.left.left = Node(2)
# root.left.left.left = Node(1)
# root.right = Node(5)
# root.right.right = Node(6)
# root.right.right.right = Node(7)

root = Node(10)
root.left = Node(8)
root.left.left = Node(7)
root.left.left.left = Node(6)
root.left.left.left.left = Node(5)


nRoot = getNewRoot(root)
printPreOrder(nRoot)

