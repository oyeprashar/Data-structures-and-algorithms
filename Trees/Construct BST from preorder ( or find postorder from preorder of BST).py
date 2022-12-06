INT_MAX = 3**38
INT_MIN = -3**38

def postOrder(root,ans):
    if root:
        postOrder(root.left)
        postOrder(root.right)
        ans.apppend(root.data)

def buildTree(currIndex,max1,min1,arr):

    if currIndex[0] == len(arr):
        return 

    if arr[currIndex[0]] < min1 or arr[currIndex[0]] > max1:
        return 

    currNode = Node(arr[currIndex[0]])
    
    currIndex[0] += 1
    currNode.left = buildTree(currIndex,currNode.data,min1,arr)
    currNode.right = buildTree(currIndex,max1,currNode.data,arr)

    return currNode

def constructTree(pre, size):
    
    currIndex = [0]
    return buildTree(currIndex,INT_MAX,INT_MIN,pre)