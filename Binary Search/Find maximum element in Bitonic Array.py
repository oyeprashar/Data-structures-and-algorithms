def findingMax(left, right, arr):
    if left <= right:

        mid = (left + right) // 2

        # conditions to check if mid is max or not
        if mid > 0 and mid < len(arr) - 1 and arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return arr[mid]

        if mid == 0 and arr[mid] > arr[mid + 1]:
            return arr[mid]

        if mid == len(arr) - 1 and arr[mid] > arr[mid - 1]:
            return arr[mid]

        # conditions to move the pointers
        if arr[mid - 1] > arr[mid]:
            return findingMax(left, mid - 1, arr)
        else:
            return findingMax(mid + 1, right, arr)


def findMax(arr):
    ans = findingMax(0, len(arr) - 1, arr)

    return ans


arr1 = [8, 10, 20, 80, 100, 200, 400, 500, 3, 2, 1]  # working
# Output: 500

arr2 = [1, 3, 50, 10, 9, 7, 6]  # working
# Output: 50

# Corner case (No decreasing part)   # None
arr3 = [10, 20, 30, 40, 50]
# Output: 50

# Corner case (No increasing part)
arr4 = [120, 100, 80, 20, 0]  # working
# Output: 120

print(findMax(arr1))
print(findMax(arr2))
print(findMax(arr3))
print(findMax(arr4))
