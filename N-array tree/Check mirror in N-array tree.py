from collections import defaultdict

class Solution:
    def checkMirrorTree(self, n, e, A, B):
        
        tree1 = defaultdict(list)
        tree2 = defaultdict(list)
        
        index = 0
        
        while index < len(A) and index < len(B):
            tree1[A[index]].append(A[index+1])
            tree2[B[index]].append(B[index+1])
            
            index += 2
    
            
        if len(tree1) != len(tree2):
            return 0
            
        for parent in tree1:
            
            if parent not in tree2:
                return 0
        
            if tree1[parent] != tree2[parent][::-1]:
                return 0
        
        return 1