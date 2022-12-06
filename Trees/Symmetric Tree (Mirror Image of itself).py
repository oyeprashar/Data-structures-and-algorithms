def isSymmetricChecker(root1,root2):
    
    if root1 == None and root2 == None:
        return True
        
    if root1 == None or root2 == None:
        return False
    
    if root1.data != root2.data:
        return False
    
    op1 = isSymmetricChecker(root1.left,root2.right) 
    op2 = isSymmetricChecker(root1.right,root2.left)
    
    return op1 & op2

def isSymmetric(root):
    
    return isSymmetricChecker(root,root)