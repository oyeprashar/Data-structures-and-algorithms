class Solution:
    def merge(self, arr1, arr2, n, m): 
        
        arr1.sort()
        arr2.sort()
        
        # nlogn + mlogm
        
        i = len(arr1)-1
        j = 0
        
        # n+m
        while i >=0 and j < len(arr2) and arr1[i] > arr2[j]:
            
            arr1[i],arr2[j] = arr2[j],arr1[i]
            i -= 1
            j += 1
        
        arr1.sort()
        arr2.sort()
        
        # nlogn + mlogm
        
        
        # O(nlogn + mlogm + m + n)
        
        return arr1,arr2