def diagonal(root):
    
    if root == None:
        return []
        
    queue = [root]
    ans = []
    
    while len(queue) != 0:
        
        curr = queue.pop(0)
        
        while curr != None:
            ans.append(curr.data)
            
            if curr.left != None:
                queue.append(curr.left)
            
            curr = curr.right   
    return ans
    