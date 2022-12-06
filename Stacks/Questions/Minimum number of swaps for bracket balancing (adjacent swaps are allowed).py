class Solution:
    def minimumNumberOfSwaps(self,S):
        
        opening = 0
        closing = 0
        unbalanced = 0
        swaps = 0
        
        for bracket in S:
            if bracket == '[':
                opening += 1
                
                if unbalanced > 0:
                    swaps += unbalanced
                    unbalanced -= 1 
            
            else:
                closing += 1
                unbalanced = closing - opening 
        
        return swaps
        
