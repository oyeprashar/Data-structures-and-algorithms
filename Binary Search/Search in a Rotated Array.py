class Solution:

    # Binary search to find out the pivot index
    """
    Properties of a pivot index (depending upon where the pivot index is) :
        1. arr[i] > arr[i + i]
        2. arr[i] < arr[i-1]
    """
    def getPivotIndex(self, left, right, arr):

        if left > right:
            return -1

        mid = (left + right) // 2

        # conditions to check pivot index
        if mid != len(arr) - 1 and arr[mid] > arr[mid + 1]:
            return mid

        elif mid != 0 and arr[mid] < arr[mid - 1]:
            return mid - 1

        # if none of the cases were hit, we change the search space
        if arr[left] < arr[mid]: # left subarray is uniform, move to right
            return self.getPivotIndex(mid + 1, right, arr)
        else:
            # move left
            return self.getPivotIndex(left, mid - 1, arr)

    def binarySeach(self, left, right, arr, target):

        if left > right:
            return -1

        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            return self. binarySeach(left, mid - 1, arr, target)

        else:
            return self. binarySeach(mid + 1, right, arr, target)


    def search(self, arr, target):
        pivotIndex = self.getPivotIndex(0, len(arr) - 1, arr)

        """
        Important : We have to search in both of the arrays!
        Lets take the following example arr = [5, 6, 7, 8, 9, 10, 1, 2, 3], target = 3. Here the pivot element is 10
        and if we say target is less than pivot and search just in the left sub-array, we will never find it!
        """

        if pivotIndex == -1:
            return self.binarySeach(0, len(arr) - 1, arr, target)

        if arr[pivotIndex] == target:
            return pivotIndex

        leftAns = self.binarySeach(0, pivotIndex - 1, arr, target)
        rightAns = self.binarySeach(pivotIndex + 1, len(arr) - 1, arr, target)

        if leftAns == -1 and rightAns == -1:
            return -1

        if leftAns != -1:
            return leftAns

        if rightAns != -1:
            return rightAns


s = Solution()
print(s.search(arr = [5, 6, 7, 8, 9, 10, 1, 2, 3], target = 10))