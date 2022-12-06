
# APPROACH ONE USING LEVEL ORDER TRAVERSAL (TOO MUCH SPACE TAKEN)
# Time Complexity = O(N) | Space Complexity = O(N)

def LeftView(root):
    
    if root == None:
        return []
    
    queue = [root]
    ans = []
    
    while len(queue) != 0:
        
        ans.append(queue[0].data)
        sizeQ = len(queue)
        
        for _ in range(sizeQ):
            
            curr = queue.pop(0)
            
            if curr.left != None:
                queue.append(curr.left)
            
            if curr.right != None:
                queue.append(curr.right)
            
        
    return ans

# EFFICIENT APPROACH RECURSION
# Time Complexity = O(N) | Space Complexity = O(H)

def getLeftView(root,currLevel,lastLevel,ans):
    
    if root == None:
        return

    if currLevel > lastLevel[0]:
        ans.append(root.data)
        lastLevel[0] = currLevel
        
    getLeftView(root.left,currLevel+1,lastLevel,ans)
    getLeftView(root.right,currLevel+1,lastLevel,ans)

def LeftView(root):
    
    ans = []
    lastLevel = [-1]
    getLeftView(root,1,lastLevel,ans)
    return ans
