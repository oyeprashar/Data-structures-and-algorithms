def counting(root,low,high,count):
    
    if root == None:
        return 

    if root.data >= low and root.data <= high:
        count[0] += 1
    
    if root.data > low:
        # we can go and check even more smaller values only if 
        # root.data > low
        
        counting(root.left,low,high,count) 
    
    if root.data < high:
        # we can go and check even more bigger values only if 
        # root.data < high
        
        counting(root.right,low,high,count) # pruning some recursive calls
        
def getCount(root,low,high):
    
    count = [0]
    counting(root,low,high,count)
    
    return count[0]