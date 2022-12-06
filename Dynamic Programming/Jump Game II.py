# TIME COMPLEXITY = O(n) | SPACE COMPLEXITY = O(1)
class Solution:
    
    def jump(self, nums: List[int]) -> int:
        
        jumps = 0
        end = 0
        farthest = 0
        
        for i in range(len(nums)-1):
            
            farthest = max(farthest,nums[i] + i)
            
            if i == end:
                jumps += 1
                end = farthest
            
        return jumps
        
# TIME COMPLEXITY = O(n^2) | SPACE COMPLEXITY = O(n)

class Solution:
    def jump(self, nums: List[int]) -> int:
        
        memory = [3**38] * len(nums)
        
        memory[-1] = 0
        
        i = len(nums)-2
        
        while i >= 0:
            
            min1 = 3**38
            for step in range(1,nums[i]+1):
                if i + step < len(memory):
                    min1 = min(min1,memory[i+step])
                
            memory[i] = min1 + 1
            
            i -= 1
        
        # print(memory)
        
        return memory[0]