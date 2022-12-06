class Solution:
    def AlternatingaMaxLength(self, nums):
        
        inc = 1
        dec = 1
        
        for i in range(1,len(nums)):
            
            if nums[i] > nums[i-1]:
                inc = dec + 1
                
            elif nums[i] < nums[i-1]:
                dec = inc + 1
        
        return max(inc,dec)