"""
In isomorphic we have two options
    1. FLip root1's left with root2's right and root1's right with root2's left
                                or
    2. Dont flipt and compare root1's left with root2's left and root1's right with root2's right
"""
class Solution:
    
    def isIsomorphic(self, root1, root2): 
        
        # we were able to traverse both trees successfully
        if root1 is None and root2 is None:
            return True

        # if one of them was None
        if root1 is None or root2 is None:
            return False

        # data mismatch
        if root1.data != root2.data:
            return False
            
        flipRes = self.isIsomorphic(root1.left, root2.right) and self.isIsomorphic(root1.right, root2.left) 
        noFlipRes =  self.isIsomorphic(root1.left, root2.left) and self.isIsomorphic(root1.right, root2.right)
        
        return flipRes or  noFlipRes
