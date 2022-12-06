class Solution:
    
    def romanToInt(self, s: str) -> int:
        
        dict1 = {"I":1,"V":5,"X":10,"L":50,"C":100,"D": 500,"M" :1000}
        
        
        lastValue = dict1[s[-1]]
        currMax = lastValue
        currSum = lastValue
        ans = 0
        
        index = len(s) - 2
        
        while index >= 0:
            
        
            
            num = dict1[s[index]]
            
            if num < currMax:
                currSum -= num
            
            elif num > currMax:
                
                ans += currSum
                currSum = num
                currMax = num
            
            elif num == currMax:
                currSum += num
            
            index -= 1
        ans += currSum
        return ans
            
            