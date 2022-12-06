class Solution:
    
    #Function to find all possible unique subsets.
    def AllSubsets(self, arr):
        arr.sort()
        N = (1 << len(arr))
        ans = []
    
        for num in range(N): # O(logN*2^N)
            curr = []
            pos = 0
    
            while num > 0:
                if num & 1 == 1:
                    curr.append(arr[pos])
                num = num >> 1
                pos += 1
    
            ans.append(curr)
            
        ans.sort()
        #print("ans =",ans)
        finalAns = []
        
        for i in range(len(ans)-1):
            if ans[i] != ans[i+1]:
                finalAns.append(ans[i])
                
        if ans[len(ans)-2] != ans[len(ans)-1]:
            finalAns.append(ans[len(ans)-1])
            
        return finalAns

arr = ['a','b','c']
s = Solution()
print(s.AllSubsets(arr))