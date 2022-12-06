
class Solution:
        
    def trailingZeroes(self,num):
        count = 0
        x = 5
        
        while num // x > 0:
            count += (num // x)
            x *= 5
        return count

    def binarySearch(self,left,right,minZeroes,ans):
        if left <= right:
            
            mid = (left + right) // 2
            
            zeroes = self.trailingZeroes(mid)
            
            if zeroes >= minZeroes:
                # save and move to left to minimize it
                ans[0] = mid
                return self.binarySearch(left,mid-1,minZeroes,ans)
                
            else:
                return self.binarySearch(mid+1,right,minZeroes,ans)



    def findNum(self, n : int):
        # Complete this function 10**4
        left = 0 
        right = 1
        
        # we need to find a right jaha pr atleast n trailing zeroes aarha hoga 
        # usse left aur right ke biche me kahi humara answer hoga
        while self.trailingZeroes(right) < n:
            left = right
            right *= 10 
        
    
        minZeroes = n
        ans = [-1]
        self.binarySearch(left,right,minZeroes,ans)
        return ans[0]
        
        