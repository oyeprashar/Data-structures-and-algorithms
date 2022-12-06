import heapq

def sortArr(arr,k):
    
    min_heap = []
    end = min(k+1,len(arr)-1)

    for i in range(end):
        heapq.heappush(min_heap,arr[i])
    
    ans = []

    # O(n-k)logk
    for j in range(end,len(arr)):
        ans.append(heapq.heappop(min_heap))
        heapq.heappush(min_heap,arr[j])
    
    while len(min_heap) > 0:
        ans.append(heapq.heappop(min_heap))
    
    return ans 