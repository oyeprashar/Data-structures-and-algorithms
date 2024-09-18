class Solution:
    def duplicates(self, arr, n): 
        
        ans = []
        
        for i in range(len(arr)):
            num = arr[i] % n 
            
            # treat this num as index and mark visited there since range is (0, N-1) so all elements are there as index also
            arr[num] += n
           
            
        for i in range(len(arr)):

            # if an index was marked more than once, the index (element) was the repeating number (again logic due to range of num)
            if arr[i] // n > 1:
                ans.append(i)
        
        if len(ans) == 0:
            return [-1]
        
        return sorted(ans)


s = Solution()
arr = [0, 3, 1, 3]

print(s.duplicates(arr, len(arr)))
