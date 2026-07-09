class Solution:
    def minSubset(self, arr):

        arr.sort(reverse = True)
        totalSum = sum(arr)

        count = 0
        subset1Sum = 0

        for i in range(len(arr)):

            subset1Sum += arr[i]
            count += 1

            subset2Sum = totalSum - subset1Sum
            
            if subset1Sum > subset2Sum:
                return count
            
        return -1
      
