import heapq
class Item:
    def __init__(self,data,dataIndex,listIndex):
        self.listIndex = listIndex
        self.dataIndex = dataIndex
        self.data = data
    def __lt__(self,otherObject):
        return self.data < otherObject.data
min_heap = []
ans = []
inputArray = [[1,2,3],[4,5,6],[7,8,9]]


for i in range(len(inputArray)):
    data = inputArray[i][0]
    item1 = Item(data,0,i)
    heapq.heappush(min_heap,item1)

while len(min_heap) > 0:
    top = heapq.heappop(min_heap)
    ans.append(top.data)

    top.dataIndex += 1

    if top.dataIndex < len(inputArray[top.listIndex]):
        top.data = inputArray[top.listIndex][top.dataIndex]
        heapq.heappush(min_heap,top)

print(ans)