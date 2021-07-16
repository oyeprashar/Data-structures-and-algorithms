
import heapq
class Solution:
    def kthElement(self,  arr1, arr2, n, m, k):
        
        # O(logN)
        heapq.heapify(arr1)
        
        # O(logM)
        for num in arr2:
            heapq.heappush(arr1,num)
            
        if k > len(arr1) or len(arr1) == 0:
            return -1
        nk = 0
        
        # isski complexity is negligible
        while nk != k:
            
            top = heapq.heappop(arr1)
            nk += 1
        return top