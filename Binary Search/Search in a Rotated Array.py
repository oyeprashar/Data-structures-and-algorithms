class Solution:
    
    def binarySearch(self,left,right,arr,key):
        
        if left <= right:
            
            mid = (left+right) // 2
            
            if arr[mid] == key:
                return mid
            
            if key > arr[mid]:
                return self.binarySearch(mid+1,right,arr,key)
            
            else:
                return self.binarySearch(left,mid-1,arr,key) 
        
        else:
            return -1
    
    def pivot(self,left,right,arr):
        
        if left <= right:

            mid = (left+right) // 2

            # this is the logic to identify the pivot element
            if mid == 0 and arr[mid] > arr[mid+1]:
                return mid + 1

            if mid == len(arr)-1 and arr[mid] < arr[mid-1]:
                return mid

            elif arr[mid] < arr[mid-1]:
                return mid
            
            elif mid != len(arr)-1:
                if arr[mid] > arr[mid+1]:
                    return mid+1

            # this is the logic to move to search space

            if arr[mid] > arr[left]:
                # left side is uniform so we move to the right side
                return self.pivot(mid+1,right,arr)

            else:
                return self.pivot(left,mid-1,arr)

    def search(self, arr : list, l : int, h : int, key : int):
        
        
        if len(arr) == 1:
            if arr[0] == key:
                return 0
            else:
                return -1
        
        if len(arr) == 2:
            if arr[0] == key:
                return 0
            if arr[1] == key:
                return 1
            else:
                return -1
        
        p = self.pivot(0,len(arr)-1,arr)
        # print(p,arr[p])
        if p == None:
            return self.binarySearch(0,len(arr)-1,arr,key)

        leftAns = self.binarySearch(0,p-1,arr,key)
        rightAns = self.binarySearch(p,len(arr)-1,arr,key)

        if leftAns == -1 and rightAns == -1:
            return -1

        if leftAns != -1:
            return leftAns

        if rightAns != -1:
            return rightAns
        
        return -1