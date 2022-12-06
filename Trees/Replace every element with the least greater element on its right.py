"""
Input: [8, 58, 71, 18, 31, 32, 63, 92, 
         43, 3, 91, 93, 25, 80, 28]

Output: [18, 63, 80, 25, 32, 43, 80, 93, 
         80, 25, 93, -1, 28, -1, -1]
"""

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

# print the inorder

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data,end = " ")
        inorder(root.right)

def insert(root,key):

    if root == None:
        return Node(key)

    if key < root.data:

        if root.left == None:
            newNode = Node(key)
            root.left = newNode
            return newNode
        else:
            return insert(root.left,key)

    if key > root.data:

        if root.right == None:
            newNode = Node(key)
            root.right = newNode
            return newNode
        else:
            return insert(root.right,key)

def InorderSuccessor(target,root):


    if target.right != None:

        curr = targetNode.right

        while curr.left != None:
            curr = curr.left

        return curr.data

    else:

        last_left_turn = -1
        curr = root

        # print(root.data,target.data)
        while curr != None and curr.data != target.data:

            if target.data < curr.data:

                last_left_turn = curr.data
                curr = curr.left

            elif target.data > curr.data:
                curr = curr.right

        # if target.data == 25:
            # print("the last_left_turn ==",last_left_turn)

        return last_left_turn



def convertArr(arr):
    root = Node(arr[-1])

    i = len(arr)-2
    arr[-1] = -1

    while i >= 0:
        target = insert(root,arr[i])
        inorderD = InorderSuccessor(target,root)

        arr[i] = inorderD
        i -= 1 

    return arr

arr = [8, 58, 71, 18, 31, 32, 63, 92, 43, 3, 91, 93, 25, 80, 28]

print(convertArr(arr))