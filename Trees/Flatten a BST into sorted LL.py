class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def printLL(head):
    while head != None:
        print(head.data,end="->")
        head = head.right

def inorderFlat(root,prev,head):

    if root != None:

        inorderFlat(root.left,prev,head)

       # print(root.data)
        if prev[0] == None:
            head[0] = root
            prev[0] = root
        
        else:
            prev[0].right = root
            prev[0] = root

        # prev[0].left = None

        inorderFlat(root.right,prev,head)


def flattenList(root):
    prev = [None]
    head = [None]
    inorderFlat(root,prev,head)
    return head[0]

root = Node(5)
root.left = Node(3)
root.left.left= Node(2)
root.left.right= Node(4)
root.right= Node(7)
root.right.left = Node(6)
root.right.right = Node(8)

head = flattenList(root)
printLL(head)

