class Solution:
    
    def knapSackHelper(self, N, W, val, wt,memory):
            
            if W == 0 or N == 0:
                return 0
            
            if memory[N][W] != -1:
                return memory[N][W]
                
            if wt[N-1] > W:
                return self.knapSackHelper(N-1,W,val,wt,memory)

                    
            memory[N][W] = max(val[N-1] + self.knapSackHelper(N,W-wt[N-1],val,wt,memory),self.knapSackHelper(N-1,W,val,wt,memory))
            return memory[N][W]
        
        
    def knapSack(self, N, W, val, wt):
        
        memory = []
        for x in range(N+1):
            list1 = []
            for y in range(W+1):
                list1.append(-1)
            memory.append(list1)
        
        return self.knapSackHelper(N,W,val,wt,memory)

