class Solution:
    def minSwaps(self, S: str) -> int:
        
        maxClosing = 0
        currClosing = 0
        
        for bracket in S:
            
            if bracket == '[':
                currClosing -= 1
            else:
                currClosing += 1
            
            maxClosing = max(maxClosing,currClosing)
    
        return (maxClosing + 1) // 2