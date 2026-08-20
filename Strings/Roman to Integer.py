"""
The logic to convert roman to int is simple :
    - We iterate from the right to left (from the end)
    - prev and total are initialised with 0
    - If currValue is less than the prev, we subtract from the total
    - If currValue is greater than the prev, we add it to the total
    - prev is always updated with the curr value
"""




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
                