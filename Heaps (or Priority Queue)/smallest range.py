import heapq
class ItemMax:
    def __init__(self, data, currIndex, arrayIndex):
        self.data = data
        self.currIndex = currIndex
        self.arrayIndex = arrayIndex

    def __lt__(self, otherObject):
        return self.data > otherObject.data


class ItemMin:
    def __init__(self, data, currIndex, arrayIndex):
        self.data = data
        self.currIndex = currIndex
        self.arrayIndex = arrayIndex

    def __lt__(self, otherObject):
        return self.data < otherObject.data


def smallestRange(numbers):
    min_heap = []
    max_heap = []

    for i in range(len(numbers)):
        num = numbers[i][0]
        currIndex = 0
        arrayIndex = i
        obj1 = ItemMin(num, currIndex, arrayIndex)
        obj2 = ItemMax(num, currIndex, arrayIndex)
        heapq.heappush(min_heap, obj1)
        heapq.heappush(max_heap, obj2)

    minRange = 3 ** 38
    ans = [0, 0]

    while True:

        minTop = heapq.heappop(min_heap)
        min1 = minTop.data
        max1 = max_heap[0].data

        if max1 - min1 < minRange:
            minRange = max1 - min1
            ans[0] = min1
            ans[1] = max1

        if minTop.currIndex + 1 < len(numbers[minTop.arrayIndex]):
            newCurrIndex = minTop.currIndex + 1
            newData = numbers[minTop.arrayIndex][newCurrIndex]

            # for min_heap
            minTop.data = newData
            minTop.currIndex = newCurrIndex
            heapq.heappush(min_heap, minTop)

            # for max_heap
            objNew = ItemMax(newData, newCurrIndex, minTop.arrayIndex)
            heapq.heappush(max_heap, objNew)

        else:
            break

    return ans