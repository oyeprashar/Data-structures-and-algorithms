"""
Input:
        10
       /  \
      8    12
     /
    3
    
Output: 3->8 8->10 10->12 12->-1
"""

class Node:
    def __init__(self,data):
        self.data = data 
        self.left = None
        self.right = None
        self.next = None

def inorder_checker(root):

    if root:

        inorder_checker(root.left)
        if root.next != None:
            print(root.data,root.next.data)
        else:
            print(root.data,None)
        inorder_checker(root.right)

def inorder(root,prev):

    if root:
        inorder(root.left,prev)

        if prev[0] != None:
            prev[0].next = root

        prev[0] = root
        
        inorder(root.right,prev)

def fillInorder(root):
    prev = [None]
    inorder(root,prev)
    prev[0].next = Node(-1)


root = Node(10)
root.left = Node(8)
root.left.left = Node(3)
root.right = Node(12)
fillInorder(root)
inorder_checker(root)
