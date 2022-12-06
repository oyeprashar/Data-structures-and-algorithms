class Solution:
    def trappingWater(self, height,n):
        
        if len(height) == 1 or len(height) == 2:
            return 0 
        
        left = [0] * len(height)
        
        left[0] = height[0]
        
        for i in range(1,len(height)):
            left[i] = max(left[i-1],height[i])
        
        right = [0] * len(height)
        
        right[-1] = height[-1]
        
        for j in range(len(height)-2,-1,-1):
            right[j] = max(right[j+1],height[j])
        
        totalWater = 0 
        
        for x in range(1,len(height)-1):
            waterLevel = min(left[x-1],right[x+1])
                        
            if height[x] < waterLevel:
                totalWater += waterLevel - height[x]
        
        return totalWater
