"""
Minimum adjacent merge operations to make an array palindromic
"""

def countOperations(arr):

    i = 0
    j = len(arr)-1
    count = 0

    while i < j:

        if arr[i] == arr[j]:
            i += 1
            j -= 1

        elif arr[i] < arr[j]:
            arr[i+1] += arr[i]
            i += 1
            count += 1

        else:
            arr[j-1] += arr[j]
            j -= 1
            count += 1

    return count

arr = [15, 4, 15]
print(countOperations(arr))

arr = [1, 4, 5, 1]
print(countOperations(arr))

arr = [11, 14, 15, 99]
print(countOperations(arr))

arr = [1, 4, 5, 9, 1]
print(countOperations(arr))




