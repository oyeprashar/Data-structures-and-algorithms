"""
==== ALGORITHM FOR SHELL SORT ====
>> First we find the initial gap by len(arr) // 2
>> While gap > 0:

    # check the array in from left to right
    =>while j < len(arr):
        >> check elements from left to right. i=0 and j = gap. Increment i and j by once and swap if arr[i] >arr[j]

    # check the array from last possible position to i to left of array
    => while i - gap != -1:
        >> is arr[i-gap] > arr[i] swap
        >> decrement i by 1


Time Complexity:Worst case => O(n2) |Average case => O(n2) |Best case => O(n2) |Space Complexity = O(1)| Inplace Sorting = YES  | Stable = NO
"""
def shellSort(arr):
    gap = len(arr) // 2

    while gap > 0:
        i = 0
        j = gap

        while j < len(arr):

            if arr[i] >arr[j]:
                arr[i],arr[j] = arr[j],arr[i]
            
            i += 1
            j += 1

        while i - gap != -1:

            if arr[i - gap] > arr[i]:
                arr[i-gap],arr[i] = arr[i],arr[i-gap]
            i -= 1

        gap //= 2


arr = [99,88,77,66,11]
arr2 = [9,8,3,7,5,6,4,1]

shellSort(arr)
shellSort(arr2)
print(arr)
print(arr2)


































