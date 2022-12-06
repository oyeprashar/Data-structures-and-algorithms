import math
import heapq

class Item:
    def __init__(self,data,index):
        self.data = data
        self.index = index
    
    def __lt__(self,otherObject):
        
        return self.data < otherObject.data

# formula is √(x1 - x2)2 + (y1 - y2)2).
# x1 and y1 are the first and second elements of the current list
# x2 and y2 both are 0 as we are finding the distance from the origin

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        min_heap = []
        
        for index,list1 in enumerate(points):
            a = list1[0]
            b = list1[1]
            
            num = a**2+ b**2
        
            
            dist = math.sqrt(num)
        
            currObject = Item(dist,index)
            min_heap.append(currObject)
        
        heapq.heapify(min_heap)
        
        ans = []
        count = 0
        
            
        while len(min_heap) > 0 and count != k:
            count += 1
            top= heapq.heappop(min_heap)
            
            index = top.index
            ans.append(points[index])
            
            
            
        return ans