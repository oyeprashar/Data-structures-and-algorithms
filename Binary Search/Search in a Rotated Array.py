#User function Template for python3
class Solution:
    def binarySearch(self,left,right,arr,key):
        if left <= right:
    
            mid = (left+right)//2 
    
            if arr[mid] == key:
                return mid
    
            if key > arr[mid]:
                return self.binarySearch(mid+1,right,arr,key)
            else:
                return self.binarySearch(left,mid-1,arr,key)
        else:
            return -1
    
    def findThePivot(self,left,right,arr):
    
        if left <= right:
    
            mid = (left+right) // 2
    
            if mid > 0 and arr[mid] < arr[mid-1]:
                return mid
    
            elif mid < len(arr)-1 and arr[mid+1] < arr[mid]:
                return mid + 1
    
            elif arr[mid] > arr[left]: # if this is the case it means that the left side of the array is uniform, move to right
    
                return self.findThePivot(mid+1,right,arr)
    
            else: # else right is uniform, check for pivot in the left part
    
                return self.findThePivot(left,mid-1,arr)
        else:
            return -1

    def search(self, arr : list, l : int, h : int, key : int):
        p = self.findThePivot(0,len(arr)-1,arr)
        if p == -1:
            return self.binarySearch(0,len(arr)-1,arr,key)
    
        else:
            ans1 = self.binarySearch(0,p,arr,key)
            ans2 = self.binarySearch(p+1,len(arr)-1,arr,key)
            if ans1 == -1 and ans2 == -1:
                return -1
            else:
                if ans1 != -1:
                    return ans1
                else:
                    return ans2
            
            
            