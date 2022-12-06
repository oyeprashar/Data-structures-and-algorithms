INT_MAX = 3**38
INT_MIN = -3**38

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:


        maxArr = [INT_MIN,INT_MIN,INT_MIN]
        minArr = [INT_MAX,INT_MAX]

        for num in nums:
            
            if num > maxArr[0]:
                maxArr[2] = maxArr[1]
                maxArr[1] = maxArr[0]
                maxArr[0] = num
                
            elif num > maxArr[1]:
                maxArr[2] = maxArr[1]
                maxArr[1] = num
            
            elif num > maxArr[2]:
                maxArr[2] = num
            
            
            if num < minArr[0]:
                minArr[1] = minArr[0]
                minArr[0] = num
            
            elif num < minArr[1]:
                minArr[1] = num
            
        
        op1 = maxArr[0] * maxArr[1] * maxArr[2]
        op2 = minArr[0] * minArr[1] * maxArr[0]
        
        return max(op1,op2)
        
        
            