class Solution:    
   
    def minimumPlatform(self,n,arr,dep):
        
        if len(arr) == 1:
            return 1
        
        arr.sort()
        dep.sort()
        
        currRequired = 1
        maxRequired = 1
        
        i = 1
        j = 0
        
        while i < len(arr) and j < len(arr):
            
            # if new train has come and old train is still at the platform, we need one more platform
            if arr[i] <= dep[j]:
                i += 1
                currRequired += 1
                maxRequired = max(maxRequired,currRequired)
            
            else:
                # else we need to depart the old train and free the platform
                j += 1
                currRequired -= 1
            
        return maxRequired