"""
Convert post-fix expression to expression tree
A 2 ^ 2 A * B * - B 2 ^ + A B - /
"""

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

def generateTree(str1):

    stack = []
    operator = set(['/','+','-','*','^'])

    for char in str1:

        if char not in operator: # i.e. it is an operand then it goes to the stack
            # print(char,operator)
            stack.append(Node(char))

        else:
            top1 = stack.pop()
            top2 = stack.pop()
            currNode = Node(char)
            currNode.right = top1
            currNode.left = top2
            stack.append(currNode)

    # print(len(stack))

    return stack[0]

str1 = "A2^2A*B*-B2^+AB-/"
root = generateTree(str1)
inorder(root)
# print(root.data)