class Solution:
    def maxProfit(self, prices):
        
        left = [0] * len(prices)
        right = [0] * len(prices)
        
        leftMin = prices[0]
        
        for i in range(1,len(left)):
            
            leftMin = min(leftMin,prices[i])
            left[i] = max(left[i-1],prices[i]-leftMin)
            
        
        rightMax = prices[-1]
        for j in range(len(prices)-2,-1,-1):
            
            rightMax = max(rightMax,prices[j])
            right[j] = max(right[j+1],rightMax-prices[j])
        
        profit = 0
        
        for c in range(len(prices)):
            
            op1  = 0    
            if c - 1 >= 0:
                op1 = left[c-1]
            
            op2 = right[c]
            
            profit = max(profit,(op1+op2))
        
        return profit
            
            