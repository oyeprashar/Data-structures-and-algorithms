class Solution:
    
    def reverse(self,start,arr):
        end = len(arr)-1
        
        while start < end:
            arr[start],arr[end] = arr[end],arr[start]
            start += 1
            end -= 1
    
    def nextPermutation(self, N, arr):
        i = None
        
        index = len(arr)-2
        
        while index >= 0:
            if arr[index] < arr[index+1]:
                i = index
                break 
            index -= 1
        
        if i == None:
            return arr[::-1]
        
        index = len(arr)-1
        j = None
        
        while index >= 0:
            if arr[index] > arr[i]:
                j = index
                break 
            index -= 1
        
        arr[i],arr[j] = arr[j],arr[i]
        self.reverse(i+1,arr)
        
        return arr
        