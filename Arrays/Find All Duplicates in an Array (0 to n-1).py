class Solution:
    def duplicates(self, arr, n): 
    	
    	ans = []
    	
    	for i in range(len(arr)):
    	    num = arr[i] % n 
    	    
    	    arr[num] += n
    	   
    	    
        for i in range(len(arr)):
            if arr[i] // n > 1:
                ans.append(i)
        
        if len(ans) == 0:
            return [-1]
        
        return sorted(ans)
