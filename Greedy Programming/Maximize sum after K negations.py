"""
Maximise the sum such that we MUST do k flips 

Approach :
  - sort the array and flip the neg numbers from left to right
  - if negCount == k return the sum of array
  - if even number of flips are left, we can say we flip and flipped the number back (effectively no change) and return the sum. 
  - if we odd number of flip left, sort the array, flip the 0th index, return the sum


Approach works because
  1. if k > negCount <--- nice! We simply flip all the neg numbers
  2. if k < negCount <--- okay, we flip what we can and k becomes zero!
"""


class Solution:
    def maximizeSum(self, arr, n, k):

        negCount = 0
        index = 0
        arr.sort()

        # arr is sorted so we processed smallest numbers first and make them positive
        while index < len(arr) and negCount < k:

            if arr[index] < 0:
                arr[index] *= -1
                negCount += 1
                
            index += 1

      
        if negCount == k or (k - negCount) % 2 == 0:
            return sum(arr)
        
        else:
            arr.sort() # since we negated
            arr[0] *= -1
            return sum(arr)
          
