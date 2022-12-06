class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        ans = set()
        
        for i in range(len(nums)):
            
            currNum = abs(nums[i])
            index = currNum-1
            
            if nums[index] < 0:
                ans.add(currNum)
            
            else:
                nums[index] = -1*nums[index]
            
        
        return ans
            
        