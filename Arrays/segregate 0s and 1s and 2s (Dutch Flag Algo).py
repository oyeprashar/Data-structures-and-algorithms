class Solution:
    def sort012(self,arr,n):
        low = 0 
        mid = 0
        high = len(arr)-1
        
        while mid <= high:
    
            if arr[mid] == 0:
                arr[mid],arr[low] = arr[low],arr[mid]
                mid += 1
                low += 1
            
            elif arr[mid] == 1:
                mid += 1
            
            elif arr[mid] == 2:
                arr[mid],arr[high] = arr[high],arr[mid]
                high -= 1
            