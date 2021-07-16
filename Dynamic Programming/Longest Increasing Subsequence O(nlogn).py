# Longest Increasing Subsequence | Time Complexity = O(nlogn) | Space Complexity = O(n)

def binarySearch(left, right, arr, key, res):
    if left <= right:

        mid = (left + right) // 2

        if arr[mid] >= key:
            res[0] = mid
            # we move to the left to minimize this
            return binarySearch(left, mid - 1, arr, key, res)

        else:
            # move right to find a number greator than this
            return binarySearch(mid + 1, right, arr, key, res)

        return -1

# finding the smallest number greator than key
def search(key, arr):
    res = [-1]
    binarySearch(0, len(arr) - 1, arr, key, res)
    return res[0]


def LIS(arr):
    sequence = []
    sequence.append(arr[0])

    for i in range(1, len(arr)):
        if arr[i] > sequence[-1]:
            sequence.append(arr[i])
        else:
            justGreaterIndex = search(arr[i], sequence)
            sequence[justGreaterIndex] = arr[i]

    return len(sequence)

arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
print(LIS(arr))