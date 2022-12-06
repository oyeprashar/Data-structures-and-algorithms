class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
    
        intervals = []
        
        for i in range(len(ranges)):
            lower = i - ranges[i]
            upper = i + ranges[i] 
            intervals.append([lower,upper])
            
        intervals.sort()
        
        
        index = 0
        min1 = 0
        max1 = 0
        open1 = 0
        
        while max1 < n:
            
            while index <= n:
                if intervals[index][0] <= min1 and intervals[index][1] > max1:
                    max1 = intervals[index][1]
                    
                elif intervals[index][0] > min1:
                    break
                    
                index += 1
                

            if max1 == min1:
                return -1
        
            min1 = max1 
            open1 += 1
        
        return open1
        