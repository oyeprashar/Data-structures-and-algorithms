class Solution:
    def fourSum(self, arr, k):
        
        total = k
        arr.sort()
        ans = []
        
        for i in range(len(arr)-3):
            for j in range(i+1,len(arr)-2):
                
              
                curr = []
                target = total - (arr[i] + arr[j])
                left = j+1
                right = len(arr)-1
                
                while left < right:
                    
                    if arr[left] + arr[right] + arr[i] + arr[j] == total:
                        ans.append([arr[i],arr[j],arr[left],arr[right]])
                        left += 1
                        right -= 1
                        
                    elif arr[left] + arr[right] + arr[i] + arr[j] > total:
                        right -= 1
                    
                    else:
                        left += 1
                        
        ans = sorted(ans)
        n = len(ans) - 1
        
        while n > 0:
        
            if ans[n] == ans[n-1]:
                ans.pop(n)
            n -= 1
        
        return len(ans),ans


target = 179
arr = [88, 84, 3, 51, 54, 99, 32, 60, 76, 68, 39, 12, 26, 86, 94, 39, 95, 70, 34, 78, 67, 1, 97, 2, 17, 92, 52]
s = Solution()
print(s.fourSum(arr,target))