# User function Template for python3
import heapq

class Pair:
    def __init__(self, data, dataIndex, listIndex):
        self.listIndex = listIndex
        self.dataIndex = dataIndex
        self.data = data

    def __lt__(self, otherObject):
        return self.data < otherObject.data

def kthSmallest(mat, n, k):
    min_heap = []
    ans = []

    for i in range(n):
        data = mat[i][0]
        pair1 = Pair(data, 0, i)
        heapq.heappush(min_heap, pair1)
    count = 0

    while len(min_heap) > 0:
        top = heapq.heappop(min_heap)
        ans.append(top.data)
        count += 1
        if count == k:
            break

        top.dataIndex += 1

        if top.dataIndex < len(mat[top.listIndex]):
            top.data = mat[top.listIndex][top.dataIndex]
            heapq.heappush(min_heap, top)
    return ans[k - 1]

