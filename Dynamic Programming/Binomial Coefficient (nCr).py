class Solution:
    def factorialHelper(self,num,memory):
        
        if num == 0 or num == 1:
            return 1
        
        if memory[num] != -1:
            return memory[num]
        
        memory[num] = num * self.factorialHelper(num-1,memory)
        
        return memory[num]
        
    def factorial(self,num):
        memory = [-1] * (num+1)
        return self.factorialHelper(num,memory)
        
    def nCr(self, n, r):
        
        if r > n:
            return 0
        
        nfact = self.factorial(n) 
        rFact = self.factorial(r)
        nrFact = self.factorial(n-r)
        
        return (nfact // (nrFact*rFact)) % 1000000007
