class Solution:
    #Function to return the lowest common ancestor in a Binary Tree.
    
    def lca(self,root, n1, n2):
        if root == None:
            return None
        
        if root.data == n1:
            return root
        
        if root.data == n2:
            return root
        
        op1 = self.lca(root.left,n1,n2)
        op2 = self.lca(root.right,n1,n2)
        
        if op1 == None and op2 == None:
            return None
        
        if op1 != None and op2 != None:
            return root
        
        if op1 != None:
            return op1
            
        if op2 != None:
            return op2