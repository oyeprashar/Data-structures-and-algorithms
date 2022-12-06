
from typing import get_args


class Node:
    def __init__(self,data):
        self.data = data
        self.left = None 
        self.right = None

def preorder(root):

    if root:
        print(root.data,end = " ")
        preorder(root.left)
        preorder(root.right)


def findEnd(i,j,str1):

    stack = []

    for x in range(i,j+1):

        if str1[x] == '(':
            stack.append(str1[x])
        
        elif str1[x] == ')':
            stack.pop()

            if len(stack) == 0:
                return x 
            

def generateTree(i,j,str1):

    if str1[i] == '(' or str1[i] == ')':
        return generateTree(i+1,j,str1)
    
    currNode = Node(int(str1[i]))

    if i + 1 < len(str1) and str1[i+1] == '(':
        startLeft = i + 1
        endLeft = findEnd(i+1,j,str1)

        currNode.left = generateTree(startLeft,endLeft,str1)

        if endLeft + 1 and str1[endLeft + 1] == '(':
            startRight = endLeft + 1
            endRight = findEnd(startRight,j,str1)

            currNode.right = generateTree(startRight,endRight,str1)
        
    return currNode

str1 = "4(2(3)(1))(6(5))"
root = generateTree(0,len(str1)-1,str1)

preorder(root)

 



