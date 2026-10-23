"""
If,
    number of rows = n
    number of cols = m

    time complexity is O(nm * logn)

    There will always me n number of elements in the heap so logn for that and then we process all the elements so n*m
    and both are nested
"""


import heapq

class Item:

    def __init__(self, row, col, value):
        self.row = row
        self.col = col
        self.value = value

    def __lt__(self, other):
        return self.value <= other.value

class Solution:

    def mergeArrays(self, mat):

        minHeap = []

        for row in range(len(mat)):
            heapq.heappush(minHeap, Item(row, 0, mat[row][0]))

        ans = []

        while minHeap:

            top = heapq.heappop(minHeap)
            ans.append(top.value)

            if top.row < len(mat) and top.col + 1 < len(mat[top.row]):
                newItem = Item(top.row, top.col + 1, mat[top.row][top.col + 1])
                heapq.heappush(minHeap, newItem)

        return ans

s = Solution()
print(s.mergeArrays([[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]))






