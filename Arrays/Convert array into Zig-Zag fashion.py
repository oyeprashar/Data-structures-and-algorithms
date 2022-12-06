class Solution:

    def zigZag(self,arr, n):

    i = 1

    while i < len(arr)-1:
        
        if arr[i-1] > arr[i]:
            arr[i],arr[i-1] = arr[i-1],arr[i]

        if i + 1 < len(arr) and arr[i+1] > arr[i]:
            arr[i],arr[i+1] = arr[i+1],arr[i]

        i += 2

        return arr