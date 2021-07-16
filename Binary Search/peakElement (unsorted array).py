"""
==== Finding the peak element in an unsorted array ====
There are two thing we need to keep in mind, 1) logic to identify the peak | 2) logic to change the search space

NOTE: If len(arr) == 1, we just return 0 without calling our binarySearch since a array with just one element cannot have a peak

- LOGIC TO IDENTIFY THE PEAK ELEMENT -
-> if the mid is not at one of the extreme ends and element at mid is greator than element at mid - 1 and mid + 1, then this element is peak
-> if mid is at index 0 and greator than mid+1 then this is the peak
-> if mid is at len(arr)-1 and it is greator than element at mid-1 then this is the peak

- LOGIC TO MOVE THE SEARCH SPACE
-> if mid > 0 and mid-1 > mid +1, we search in space left,mid-1. 
   NOTE : mid > 0 because if we dont check this and mid is 0, then mid-1 = -1 and we would be compairing last element with mid+1

-> else move to mid+1,right

"""
class Solution:   
    def binarySearch(self,left,right,arr):
        
        if left <= right:
            
            mid = (left + right) // 2
            
            # LOGIC TO IDENTIFY THE PEAK ELEMENT
            if mid > 0 and mid < len(arr)-1 and arr[mid] > arr[mid-1] and arr[mid] > arr[mid+1]:
                return mid
            
            if mid == 0 and arr[mid] > arr[mid+1]:
                return mid
            
            if mid == len(arr)-1 and arr[mid] > arr[mid-1]:
                return mid
            
            # LOGIC TO MOVE LEFT OR RIGHT
            # we move to the part which is more promising to have a peak element
            # if mid -1 is bigger we move to left part else we move to the right part
            
            if mid > 0 and arr[mid-1] > arr[mid+1]:
                return self.binarySearch(left,mid-1,arr)
            else:
                return self.binarySearch(mid+1,right,arr)
        
        else:
            return -1
        
    def peakElement(self,arr, n):
        
        if len(arr) == 1:
            return 0 # NO PEAK
        
        else:
            return self.binarySearch(0,len(arr)-1,arr)


#{ 
#  Driver Code Starts
if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = Solution().peakElement(arr.copy(), n)
        flag = False
        if index<0 or index>=n:
            flag = False
        else:
            if index == 0 and n==1:
                flag = True
            elif index==0 and arr[index]>=arr[index+1]:
                flag = True
            elif index==n-1 and arr[index]>=arr[index-1]:
                flag = True
            elif arr[index-1] <= arr[index] and arr[index] >= arr[index+1]:
                flag = True
            else:
                flag = False

        if flag:
            print(1)
        else:
            print(0)
# Contributed by: Harshit Sidhwa

# } Driver Code Ends