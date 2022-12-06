class Solution:
    def countWays(self,n,k):
        
        if n == 0:
            return 0 
        
        if n == 1:
            return k 
        
        same = k 
        diff = k*(k-1)
        
        for i in range(3,n+1):
            prevDiff = diff
            diff = ((same + diff) * (k -1)) 
            same = prevDiff*1
            
        return same+diff