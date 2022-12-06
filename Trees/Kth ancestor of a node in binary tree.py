class Node:

    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def getAncestor(root,key,k,currPath,ans):

    if root == None:
        return 

    currPath.append(root.data)
    getAncestor(root.left,key,k,currPath,ans)
    getAncestor(root.right,key,k,currPath,ans)

    if root.data == key:
        if len(currPath) < k:
            ans[0] = -1
        else:
            ans[0] = currPath[len(currPath)-k-1]

        return 

    currPath.pop()

def kthAncestor(root,key,k):

    currPath = []
    ans = [-1]
    getAncestor(root,key,k,currPath,ans)
    return ans[0]


root = Node(1)
root.left = Node(2)
root.left.left = Node(4)
root.left.right = Node(5)
root.right = Node(3)

print(kthAncestor(root,5,2))