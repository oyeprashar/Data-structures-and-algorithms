class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def findSize(root):

    if root == None:
        return 0

    return findSize(root.left) + 1 + findSize(root.right)

def findElements(root,count,size,arr):

    if root:
        findElements(root.left,count,size,arr)

        count[0] += 1

        if count[0] == size // 2:
            arr[0] = root.data

        if count[0] == (size//2) + 1:
            arr[1] = root.data

        findElements(root.right,count,size,arr)

def findMedian(root):

    if root.left == None and root.right == None:
        return root.data

    size = findSize(root)
    arr = [-1,-1]
    count = [0]

    findElements(root,count,size,arr)

    if size % 2 == 0:
        return sum(arr) // 2

    else:
        return arr[1]


root1 = Node(20)
root1.left = Node(8)
root1.left.left = Node(4)
root1.left.right = Node(12)
root1.left.right.left = Node(10)
root1.left.right.right = Node(14)
root1.right = Node(22)

print(findMedian(root1))

root2 = Node(6)
root2.left = Node(3)
root2.left.left = Node(1)
root2.left.right = Node(4)
root2.right = Node(8)
root2.right.left = Node(7)

print(findMedian(root2))
