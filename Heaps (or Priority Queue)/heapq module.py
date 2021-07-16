"""
Heapq is the module used to implement heaq
    1) heapq.heapify(arrayName) : makes min heap in place
    2) heap.heappush(arrayName, item) : pushes item to the heap and heapifies the array
    3) heap.heappop(arrayName) : deletes the min element and returns it, also heapifies the rest of the array
"""
import heapq

array1 = [11,2,4,66,0]
print("ORIGNAL INPUT ARRAY : ",array1)
heapq.heapify(array1)
print("MIN HEAP : ",array1)

heapq.heappush(array1,-1)
print("PUSHING -1 IN THE HEAP:",array1)

print("POPING  :",heapq.heappop(array1))
print("ARRAY AFTER POPPING : ",array1)