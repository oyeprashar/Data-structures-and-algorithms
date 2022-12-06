import heapq

class Item:
    
    def __init__(self,char,freq):
        self.char = char 
        self.freq = freq
    
    def __lt__(self,otherObj):
        return self.freq > otherObj.freq 
    
class Solution:
    def reorganizeString(self, str1: str) -> str:
        dict1 = {}
        max_heap = []
        
        for char in str1:
            
            if char in dict1:
                dict1[char] += 1
            else:
                dict1[char] = 1
        
        for char in dict1:
            currObj = Item(char,dict1[char])
            heapq.heappush(max_heap,currObj)
        
        ans = ""
        
        while len(max_heap) > 1:
            
            top1 = heapq.heappop(max_heap)
            top2 = heapq.heappop(max_heap)
            
            ans += top1.char
            top1.freq -= 1
            if top1.freq > 0:
                heapq.heappush(max_heap,top1)
            
            ans += top2.char
            top2.freq -= 1
            if top2.freq > 0:
                heapq.heappush(max_heap,top2)
    
        
        if len(max_heap) > 0:
            if max_heap[0].freq > 1:
                return ""
            else:
                ans += max_heap[0].char
        return ans