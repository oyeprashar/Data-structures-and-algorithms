class Solution:
    
    def kthLargestHelper(self,root, k,count,ans):
        
        if root != None:
            
            self.kthLargestHelper(root.right, k,count,ans)
            
            count[0] += 1
            
            if count[0] == k:
                ans[0] = root.data
                return 
            
            self.kthLargestHelper(root.left, k,count,ans)
        
    
    def kthLargest(self,root, k):
        
        count = [0]
        ans = [None]
        
        self.kthLargestHelper(root, k,count,ans)
        
        return ans[0]