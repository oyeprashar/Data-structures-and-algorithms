def deletionBT(root, key):
    
    if root == None:
        return root
    
    if root.left == None and root.right == None:
        
        if root.data == key:
            return None
        else:
            return root
    
    
    # step 1 : find the node that we want to deleted and the deepest node
    
    target = None
    deepest = None
    queue = [root]
    
    while len(queue) != 0:
        
        curr = queue.pop(0)
        
        if curr.data == key:
            target = curr
        
        if curr.left != None:
            queue.append(curr.left)
        
        if curr.right != None:
            queue.append(curr.right)
        
    target.data = curr.data
    deepest = curr
    # curr is the address of the deepest node
    
    queue = [root]
    
    while len(queue) != 0:
        
        curr = queue.pop(0)
        
        if curr.left != None:
            
            if curr.left == deepest:
                curr.left = None
                return root
            else:
                queue.append(curr.left)
            
        
        if curr.right != None:
            
            if curr.right == deepest:
                curr.right = None
                return root
            
            else:
                queue.append(curr.right)
            
    
    return root
        
        