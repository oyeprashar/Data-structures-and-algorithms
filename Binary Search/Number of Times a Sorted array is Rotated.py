#User function Template for python3
class Solution:
    def findingPivot(self,left,right,arr):
    	if left <= right:
    		mid = (left + right) // 2
    
    		if mid < right and arr[mid] > arr[mid + 1]:
    			return mid
    		elif mid > left and arr[mid - 1] > arr[mid]:
    			return mid - 1
    
    		elif arr[mid] > arr[left]:
    			# this means left part is uniform so we move to right to find the piviot
    			return self.findingPivot(mid+1,right,arr)
    		else:
    			return self.findingPivot(left,mid-1,arr)
    	else:
    	    return -1

    def findKRotation(self,arr,  n):
        left = 0
	    right = len(arr) - 1
	    pivot = self.findingPivot(left,right,arr)
	    if pivot != -1:
	        return pivot + 1
	    return 0