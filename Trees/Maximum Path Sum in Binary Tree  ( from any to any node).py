class Solution:
    
    def maxPathSumHelper(self,root,ans):
        
        if root == None:
            return 0
        
        if root.left == None and root.right == None:
            ans[0] = max(ans[0],root.val)
            return root.val
    
        
        lmax = max(self.maxPathSumHelper(root.left,ans),0)  
        rmax = max(self.maxPathSumHelper(root.right,ans),0)
        
        
        ans[0] = max(ans[0],root.val+lmax+rmax)
        
        
        return root.val + max(lmax,rmax)
    
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        if root == None:
            return 0
        
        
        ans = [-3**38]
        self.maxPathSumHelper(root,ans)

        return ans[0]
        