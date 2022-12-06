def bToDLLHelper(root,prevNode,head):
    
    if root != None:
        
        bToDLLHelper(root.left,prevNode,head)
        
        if prevNode[0] == None:
            head[0] = root
            
        else:
            prevNode[0].right = root
            root.left = prevNode[0]
        
        prevNode[0] = root
        
        bToDLLHelper(root.right,prevNode,head)
        

def bToDLL(root):
    
    prevNode = [None]
    head = [None]
    
    bToDLLHelper(root,prevNode,head)
    
    return head[0]