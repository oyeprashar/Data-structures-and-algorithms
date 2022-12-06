class Solution:
    def findSwapValues(self,a, n, b, m):
        a = sorted(a)
        b = sorted(b)
        
        sum1 = sum(a)
        sum2 = sum(b)
        
        target = (sum1 - sum2) / 2
        
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] - b[j] == target:
                return 1
                
            elif a[i] - b[j] > target:
                j += 1
            
            else:
                i += 1
                
        return -1