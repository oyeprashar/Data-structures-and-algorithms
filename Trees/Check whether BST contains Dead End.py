INT_MAX = 3**38
INT_MIN = -3**38

def check(root,min1,max1):
    
    if root == None:
        return False
    
    if abs(root.data - min1) == 1 and abs(root.data - max1) == 1:
        return True
    
    op1 = check(root.left,min1,root.data)
    op2 = check(root.right,root.data,max1)
    
    return op1 | op2
    
def isdeadEnd(root):
    
    return check(root,0,INT_MAX)
