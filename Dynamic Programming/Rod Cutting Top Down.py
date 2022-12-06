class Solution:
    def solver(self,n,price,memory):
        
        if n == 0:
            return 0
         
        if memory[n] != -1:
            return memory[n]
        
        ans = -3**38
        
        for i in range(len(price)):
            currCut = n - (i+1)
            if currCut >= 0:
                res = price[i] + self.solver(currCut,price,memory)
                ans = max(ans,res)
            
        memory[n] = ans
        
        return ans
        
    def cutRod(self, price, n):
        
        memory = [-1] * (n+1)
        return self.solver(n,price,memory)
