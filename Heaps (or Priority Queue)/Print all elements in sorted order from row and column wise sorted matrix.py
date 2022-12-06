"""
Input: mat[][]  =  { {10, 20, 30, 40},
                     {15, 25, 35, 45},
                     {27, 29, 37, 48},
                     {32, 33, 39, 50},
                   };
"""
import heapq

class Item:
    def __init__(self,rowIndex,colIndex,value):
        self.rowIndex = rowIndex
        self.colIndex = colIndex 
        self.value = value 
    
    def __lt__(self,otherObj):
        return self.value < otherObj.value

def mergeKsortedArrays(mat):
    
    min_heap = []

    for row in range(len(mat)):
        rowIndex = row 
        colIndex = 0 
        value = mat[row][0]

        currItem = Item(rowIndex,colIndex,value)
        heapq.heappush(min_heap,currItem)

    ans = []

    while len(min_heap) > 0:

        top = heapq.heappop(min_heap)

        ans.append(top.value)

        if top.colIndex + 1 < len(mat[top.rowIndex]):
            top.colIndex += 1
            top.value = mat[top.rowIndex][top.colIndex]
            heapq.heappush(min_heap,top)
        
    
    return ans


grid =  [[10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50]]

print(mergeKsortedArrays(grid))