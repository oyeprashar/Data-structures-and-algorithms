class Solution:
    # Return True if the given trees are isomotphic. Else return False.
    def isIsomorphic(self, root1, root2): 
        if root1 == None and root2 == None:
            return True
            
        if root1 == None or root2 == None:
            return False
        
        if root1.data != root2.data:
            return False
        
        op1 = self.isIsomorphic(root1.left,root2.left) and self.isIsomorphic(root1.right,root2.right)
        op2 = self.isIsomorphic(root1.left,root2.right) and self.isIsomorphic(root1.right,root2.left)
        
        return op1 | op2