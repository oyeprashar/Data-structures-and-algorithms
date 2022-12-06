class Solution:
    
    def threeWayPartition(self, arr, a, b):
        low = 0
        mid = 0
        high = len(arr)-1

        while mid <= high:
            
            if arr[mid] < a:
                arr[mid],arr[low] = arr[low],arr[mid]
                low += 1
                mid += 1
            
            elif arr[mid] >= a and arr[mid] <= b:
                mid += 1
            
            elif arr[mid] > b:
                arr[mid],arr[high] = arr[high],arr[mid]
                high -= 1
            
        return arr