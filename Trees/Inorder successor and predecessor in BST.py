# Finding inorder sucessor and predecessor

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def minVal(root):
    ans = -1
    curr = root

    while curr != None:
        ans = curr.data
        curr = curr.left

    return ans

def maxVal(root):
    ans = -1
    curr = root

    while curr != None:
        ans = curr.data
        curr = curr.right   

    return ans



def find(root,targetNode):

    if root == None:
        return []

    pre = None
    sucessor = None

    # finding the inorder-sucessor first

    if targetNode.right != None:
        sucessor = minVal(targetNode.right)

    else:
        curr = root
        # keep a track of last left
        while curr != None:
            if targetNode.data < curr.data:
                sucessor = curr.data
                curr = curr.left

            elif targetNode.data > curr.data:
                curr = curr.right

            else:
                break


    if targetNode.left != None:
        pre = maxVal(targetNode.left)

    else:
        curr = root
        
        while curr != None:
            if targetNode.data < curr.data:
                curr = curr.left

            elif targetNode.data > curr.data:
                pre = curr.data
                curr = curr.right

            else:
                break

    return pre,sucessor


root = Node(99)
root.left = Node(80)
root.left.left = Node(70)
root.left.right = Node(85)
root.right = Node(150)
root.right.left = Node(110)
root.right.right = Node(200)

print(find(root,root.left)) 