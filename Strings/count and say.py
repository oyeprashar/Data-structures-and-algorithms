class Solution:
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return "1"
        
        prev = self.countAndSay(n-1)
        
        currChar = prev[0]
        count = 1
        curr = ""
        
        for i in range(1,len(prev)):
            
            if prev[i] == currChar:
                count += 1
            
            elif prev[i] != currChar:
                curr += str(count)
                curr += currChar
                
                currChar = prev[i]
                count = 1
            
        curr += str(count)
        curr += currChar
        
        return curr 