"""
Generating subset with bitmasking will take O(logn*2^n)
We can do this in just O(2^n) by using backtracking
"""

class Solution:

    def subsetsWithDup(self, arr):
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

        finalAns = []

        for i in range(len(ans)-1):
            if ans[i] != ans[i+1]:
                finalAns.append(ans[i])

        if ans[len(ans)-2] != ans[len(ans)-1]:
            finalAns.append(ans[len(ans)-1])

        return finalAns

arr = [2,1,2]
s = Solution()
print(s.subsetsWithDup(arr))