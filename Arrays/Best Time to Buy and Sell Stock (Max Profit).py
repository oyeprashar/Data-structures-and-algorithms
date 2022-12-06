
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min1 = 3**38
        max1 = 0
        
        for i in range(len(prices)):
            
            min1 = min(min1,prices[i])
            
            if prices[i] - min1 > 0:
                max1 = max(max1,prices[i]-min1)
        
        return max1
            
        
            