class Solution:
    
    def sortedArrayToBSTHelper(self,left,right,nums):
        
        if left > right:
            return None
    
        if right == left:
            return TreeNode(nums[right])
        
        mid = (left + right)  // 2
        
        currNode = TreeNode(nums[mid])
        
        currNode.left = self.sortedArrayToBSTHelper(left,mid-1,nums)
        currNode.right = self.sortedArrayToBSTHelper(mid+1,right,nums)
        
        return currNode
    
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        
        return self.sortedArrayToBSTHelper(0,len(nums)-1,nums)
        