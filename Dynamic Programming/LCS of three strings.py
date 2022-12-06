class Solution:

    def LCSof3(self,A,B,C,n1,n2,n3):
        
        memory = []
        
        for x in range(len(A)+1):
            mat = []
            
            for y in range(len(B)+1):
                list1 = []
                
                for z in range(len(C)+1):
                    list1.append(0)
                    
                mat.append(list1)
            memory.append(mat)
            
        for i in range(1,len(A)+1):
            for j in range(1,len(B)+1):
                for k in range(1,len(C)+1):
                    
                    if A[i-1] == B[j-1] == C[k-1]:
                        memory[i][j][k] = 1 + memory[i-1][j-1][k-1] 
                    
                    else:
                        memory[i][j][k] = max(memory[i-1][j][k],memory[i][j-1][k],memory[i][j][k-1])
        
        return memory[i][j][k]
        
    
        
        