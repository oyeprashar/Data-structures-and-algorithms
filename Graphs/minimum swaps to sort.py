class Solution:
    def minSwaps(self, nums):
        temp = []
        for index, item in enumerate(nums):
            temp.append((item, index))
        sortedTemp = sorted(temp)

        newToOldIndexDict = {}
        for i in range(len(nums)):
            newToOldIndexDict[i] = sortedTemp[i][1]

        visited = {}  # this is made a dictionary becacuse adding key value pair is more
        # efficient then appending to a list.

        ans = 0
        for j in range(len(nums)):  # checking for all the indices in the array
            curr = j
            count = 0  # count is initilized inside the for loop because we need to count for each element and we dont need its old value
            if j in visited:  # if the index is already involved in swapping ( or is in visited), we skip checking that index
                continue
            while curr != newToOldIndexDict[
                j]:  # if the new and old index are not equal, it implies that it needs swapping!
                count += 1
                j = newToOldIndexDict[j]
                visited[curr] = True
                visited[j] = True  # add this j to visited
            ans += count
        return ans
s = Solution()
arr1 = [10,19,6,3,5]
print(s.minSwaps(arr1))