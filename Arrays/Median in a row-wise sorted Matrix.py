import heapq


class Item:
    def __init__(self, value, rowIndex, colIndex):
        self.value = value
        self.rowIndex = rowIndex
        self.colIndex = colIndex

    def __lt__(self, other):
        return self.value <= other.value

class Solution:
    
    def find_median(self, mat, target_index):
        min_heap = []
        for rowIndex in range(len(mat)):
            item = Item(mat[rowIndex][0], rowIndex, 0)
            heapq.heappush(min_heap, item)

        count = 0
        while len(min_heap) > 0 and count != target_index:

            top = heapq.heappop(min_heap)
            count += 1

            if count == target_index:
                return top.value

            if top.colIndex + 1 < len(mat[top.rowIndex]):
                new_value = mat[top.rowIndex][top.colIndex + 1]
                new_item = Item(new_value, top.rowIndex, top.colIndex + 1)
                heapq.heappush(min_heap, new_item)
                
        return -1

    def median(self, mat):
        target_index = ((len(mat) * len(mat[0])) // 2) + 1
        return self.find_median(mat, target_index)


mat1 = [[1, 3, 5],
        [2, 6, 9],
        [3, 6, 9]]

mat2 = [[2, 4, 9],
        [3, 6, 7],
        [4, 7, 10]]

mat3 = [[3], [4], [8]]

s = Solution()
print(s.median(mat1))
print(s.median(mat2))
print(s.median(mat3))
