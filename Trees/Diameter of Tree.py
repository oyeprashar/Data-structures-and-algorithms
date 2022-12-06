class Solution:
    
    def height(self,root,ans):
        
        if root == None:
            return 0
            
        lHeight = self.height(root.left,ans)
        rHeight = self.height(root.right,ans)
        
        ans[0] = max(ans[0],lHeight + 1 + rHeight)
        
        return 1 + max(lHeight,rHeight)
    
    def diameter(self,root):
        
        if root == None:
            return 0
        
        ans = [-3**38]
        
        self.height(root,ans)
        
        return ans[0]
        