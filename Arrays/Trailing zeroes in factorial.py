
class Solution:

    def trailingZeroes(self, n):
        # we need to count the number of 5, 5^2, 5^3.......
        
        # count = (n/5) + (n//5^2) + (n//5^3) ... until (n//5^) > 0
        
        x = 5
        count = 0
        
        while n // x > 0:
            count += n // x
            x *= 5 
        
        return count
    	 
    	 
    	    