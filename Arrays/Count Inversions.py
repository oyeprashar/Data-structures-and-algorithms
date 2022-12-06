class Solution:
    
    def findInversions(self,arr,count):
        
        if len(arr) == 1:
            return 
    
        mid = len(arr) // 2
    
        left = arr[:mid]
        right = arr[mid:]
    
        self.findInversions(left,count)
        self.findInversions(right,count)
    
        i = 0 
        j = 0
    
        # we have to count the inversions and then we have to merge the left and right
        while i < len(left) and j < len(right):
    
            if left[i] > right[j]:
                count[0] += len(left) - i
                j += 1
            else:
                i += 1
    
    
        i = j = k = 0
    
        while i < len(left) and j < len(right):
    
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1
    
        while i < len(left):
    
            arr[k] = left[i]
            i += 1
            k += 1
    
        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    def inversionCount(self, arr, n):
        count = [0] 
        self.findInversions(arr,count)
        return count[0]

s = Solution()
arr = [2,4,1,3,5]
print(s.inversionCount(arr,len(arr)))