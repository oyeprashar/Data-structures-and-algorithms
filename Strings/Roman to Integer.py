class Solution:
    
    def romanToInt(self, s: str) -> int:
        
        roman2int = {'I':1,'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000}
        
        currMax = roman2int[s[-1]]
        currSum = roman2int[s[-1]]
        total = 0
        
        for i in range(len(s)-2,-1,-1):
            
            currNum = roman2int[s[i]]
            
            if currNum < currMax:
                currSum -= currNum 
            
            else:
                total += currSum
                currMax = currNum 
                currSum = currNum 
        
        total += currSum
        return total
                