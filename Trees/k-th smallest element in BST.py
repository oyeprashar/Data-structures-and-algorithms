class Solution:
    
    def KthSmallestElementHelper(self, root, K,count,ans):
        
        if root != None:
            self.KthSmallestElementHelper(root.left, K,count,ans)
            
            count[0] += 1
            
            if count[0] == K:
                ans[0] = root.data
                return 
            
            self.KthSmallestElementHelper(root.right, K,count,ans)
                    
    def KthSmallestElement(self, root, K): 
        if root == None:
            return root
            
        count = [0]
        ans = [None]
        
        self.KthSmallestElementHelper(root, K,count,ans)
        
        if ans[0] == None:
            return -1
        return ans[0]
