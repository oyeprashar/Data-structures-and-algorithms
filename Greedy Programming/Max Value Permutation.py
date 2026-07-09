class Solution:
    def maxValue(self, arr):

        """
        - We need to maximise summation of arr[i] * i
        - We simply need big numbers at big indices
        - That means we need to sort the array
        """
    
        arr.sort()
        total = 0
    
        for i in range(len(arr)):
            total += arr[i] * i
    
        return total % 1000000007
