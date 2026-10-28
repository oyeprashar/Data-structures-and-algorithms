"""
The approach :
    - We generate the prefix array with one extra element, while keeping zero value at the index 0
    - Then we use to loop over it to generate all the possible continuous sums
    - We use minHeap technique to figure out the kth largest
"""


import heapq

class Solution:

    def kthLargest(self, arr, k):

        # the first element is zero signifying that no elements were included

        preFixSum = [0]  * (len(arr) + 1)

        for i in range(len(arr)):
            preFixSum[i + 1] = arr[i] + preFixSum[i]

        # print("The generated prefix sum :", preFixSum)


        minHeap = []


        for i in range(len(preFixSum)):
            for j in range(i + 1, len(preFixSum)):

                currSum = preFixSum[j] - preFixSum[i]
                heapq.heappush(minHeap, currSum)

                if len(minHeap) > k:
                    heapq.heappop(minHeap)


        return minHeap[0]