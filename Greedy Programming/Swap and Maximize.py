"""
Swap the elements and maximise  |a1 – a2| + |a2 – a3| + …… + |an-1 – an| + |an – a1|

Approach :
  We want to subtract large numbers and small numbers so that output a number as large as possible
"""

class Solution:
    def maxSum(self, arr):

        arr.sort()
        newArr = []
        i = 0
        j = len(arr) - 1

        while i < j:
            newArr.append(arr[i])
            newArr.append(arr[j])
            i += 1
            j -= 1

      
        if len(arr) % 2 == 1:
            newArr.append(arr[ len(arr) // 2 ])

        total = 0
        for i in range(len(newArr) - 1):
            total += abs(newArr[i] - newArr[i + 1])

        total += abs(newArr[-1] - newArr[0])
        return total
      
